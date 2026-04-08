@app.route("/upload", methods=["POST"])
def upload():

    try:
        # =========================
        # CHECK FILE
        # =========================
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        # =========================
        # READ CSV
        # =========================
        try:
            df = pd.read_csv(file, encoding="latin1")
        except Exception as e:
            return jsonify({"error": f"CSV read error: {str(e)}"}), 400

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

            # detect score column
            if any(k in col_lower for k in ["score", "rating", "stars", "feedbackscore"]):
                score_col = col

            # detect text column
            elif any(k in col_lower for k in ["review", "text", "comment", "feedback", "message", "description"]):
                review_col = col

        print("Using score column:", score_col)
        print("Using text column:", review_col)

        # =========================
        # ANALYSIS
        # =========================
        pos_list, neg_list, neu_list = [], [], []

        for index, row in df.iterrows():

            text = ""
            score = None

            # get text
            if review_col:
                text = str(row[review_col])

            # get score
            if score_col:
                try:
                    score = float(row[score_col])
                except:
                    score = None

            # =========================
            # PRIORITY → SCORE BASED
            # =========================
            if score is not None:

                if score >= 4:
                    pos_list.append(text)
                elif score <= 2:
                    neg_list.append(text)
                else:
                    neu_list.append(text)

            # =========================
            # FALLBACK → ML TEXT
            # =========================
            elif text:

                clean_text = clean(text)
                vec = vectorizer.transform([clean_text])

                pred = model.predict(vec)[0]

                if pred == "positive":
                    pos_list.append(text)
                elif pred == "negative":
                    neg_list.append(text)
                else:
                    neu_list.append(text)

        # =========================
        # COUNTS
        # =========================
        pos = len(pos_list)
        neg = len(neg_list)
        neu = len(neu_list)

        total = pos + neg + neu

        print("POS:", pos, "NEG:", neg, "NEU:", neu)

        if total == 0:
            return jsonify({"error": "No valid data found"}), 400

        # =========================
        # KEYWORDS (REAL REASONS)
        # =========================
        pos_words = top_words(pos_list) if pos_list else []
        neg_words = top_words(neg_list) if neg_list else []
        neu_words = top_words(neu_list) if neu_list else []

        # =========================
        # METRICS
        # =========================
        metrics = generate_metrics(total)

        # =========================
        # RESPONSE
        # =========================
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
        return jsonify({"error": f"Server error: {str(e)}"}), 500
