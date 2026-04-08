
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
        # READ CSV SAFELY
        # =========================
        try:
            df = pd.read_csv(file, encoding="latin1")
        except Exception as e:
            return jsonify({"error": f"CSV read error: {str(e)}"}), 400

        if df.empty:
            return jsonify({"error": "CSV is empty"}), 400

        print("Columns:", df.columns)

        # =========================
        # DETECT TEXT OR SCORE COLUMN
        # =========================
        review_col = None
        score_col = None

        for col in df.columns:
            col_lower = col.lower()

            # TEXT COLUMN DETECTION
            if any(k in col_lower for k in [
                "review","text","comment","feedback","message","description","content"
            ]):
                review_col = col

            # SCORE COLUMN DETECTION
            if any(k in col_lower for k in [
                "score","rating","stars","rate","feedbackscore"
            ]):
                score_col = col

        print("Detected review column:", review_col)
        print("Detected score column:", score_col)

        pos_list, neg_list, neu_list = [], [], []

        # =========================
        # CASE 1: TEXT DATA
        # =========================
        if review_col:

            texts = df[review_col].dropna().astype(str)

            for text in texts:
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
        # CASE 2: NUMERIC SCORE
        # =========================
        elif score_col:

            scores = df[score_col].dropna()

            for s in scores:
                try:
                    s = float(s)

                    if s >= 4:
                        pos_list.append(str(s))
                    elif s <= 2:
                        neg_list.append(str(s))
                    else:
                        neu_list.append(str(s))

                except:
                    continue

        # =========================
        # CASE 3: FALLBACK (FIRST COLUMN)
        # =========================
        else:

            first_col = df.columns[0]
            print("Fallback column:", first_col)

            texts = df[first_col].dropna().astype(str)

            for text in texts:
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
        # CALCULATE RESULTS
        # =========================
        pos = len(pos_list)
        neg = len(neg_list)
        neu = len(neu_list)

        total = pos + neg + neu

        # =========================
        # KEYWORDS
        # =========================
        pos_words = top_words(pos_list)
        neg_words = top_words(neg_list)
        neu_words = top_words(neu_list)

        # =========================
        # METRICS
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
        return jsonify({"error": f"Server error: {str(e)}"}), 500
