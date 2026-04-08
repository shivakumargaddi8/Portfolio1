@app.route("/upload", methods=["POST"])
def upload():

    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        # =========================
        # READ CSV
        # =========================
        df = pd.read_csv(file, encoding="latin1")

        if df.empty:
            return jsonify({"error": "CSV is empty"}), 400

        print("Columns:", df.columns)

        # =========================
        # DETECT COLUMNS
        # =========================
        review_col = None
        score_col = None

        for col in df.columns:
            col_lower = col.lower()

            if any(k in col_lower for k in ["score","rating","stars"]):
                score_col = col

            if any(k in col_lower for k in ["review","text","comment","feedback","message"]):
                review_col = col

        print("Score column:", score_col)
        print("Text column:", review_col)

        pos, neg, neu = 0, 0, 0

        pos_list, neg_list, neu_list = [], [], []

        # =========================
        # LOOP EACH ROW (REAL DATA)
        # =========================
        for _, row in df.iterrows():

            text = ""
            score = None

            # get values safely
            if review_col:
                text = str(row[review_col]).strip()

            if score_col:
                try:
                    score = float(row[score_col])
                except:
                    score = None

            # =========================
            # PRIORITY → SCORE (REAL DATA)
            # =========================
            if score is not None:

                if score >= 4:
                    pos += 1
                    pos_list.append(str(score))

                elif score <= 2:
                    neg += 1
                    neg_list.append(str(score))

                else:
                    neu += 1
                    neu_list.append(str(score))

            # =========================
            # TEXT → ML ONLY IF NO SCORE
            # =========================
            elif text:

                clean_text = clean(text)
                vec = vectorizer.transform([clean_text])

                pred = model.predict(vec)[0]

                if pred == "positive":
                    pos += 1
                    pos_list.append(text)

                elif pred == "negative":
                    neg += 1
                    neg_list.append(text)

                else:
                    neu += 1
                    neu_list.append(text)

        total = pos + neg + neu

        print("REAL COUNTS →", pos, neg, neu)

        if total == 0:
            return jsonify({"error": "No valid data"}), 400

        # =========================
        # REAL KEYWORDS
        # =========================
        pos_words = top_words(pos_list) if pos_list else []
        neg_words = top_words(neg_list) if neg_list else []
        neu_words = top_words(neu_list) if neu_list else []

        # =========================
        # METRICS (ONLY DISPLAY PURPOSE)
        # =========================
        metrics = generate_metrics(total)

        return jsonify({
            "positive": pos,
            "negative": neg,
            "neutral": neu,

            "positive_words": pos_words,
            "negative_words": neg_words,
            "neutral_words": neu_words,

            **metrics
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
