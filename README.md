
function generateInsights(data) {

  // =========================
  // REAL VALUES FROM DATA
  // =========================

  const total = data.positive + data.negative + data.neutral;

  const posPct = ((data.positive / total) * 100).toFixed(1);
  const negPct = ((data.negative / total) * 100).toFixed(1);
  const neuPct = ((data.neutral / total) * 100).toFixed(1);

  // =========================
  // WORDS
  // =========================

  const posWords = data.positive_words?.join(", ") || "quality, service, performance";
  const negWords = data.negative_words?.join(", ") || "delays, issues, defects";
  const neuWords = data.neutral_words?.join(", ") || "average experience, moderate expectations";

  // =========================
  // 3-LINE SUMMARY SETS
  // =========================

  const positiveSet = [
    [
      `Customers highlighted <b>${posWords}</b> as key strengths.`,
      `This reflects strong satisfaction and a positive user experience.`,
      `Overall, it indicates trust and consistent product performance.`
    ],
    [
      `Users frequently praised <b>${posWords}</b>.`,
      `Feedback shows high confidence in quality and usability.`,
      `This suggests a reliable and well-performing product.`
    ]
  ];

  const negativeSet = [
    [
      `Customers reported issues related to <b>${negWords}</b>.`,
      `These concerns are affecting satisfaction and usability.`,
      `Immediate improvements are needed to enhance experience.`
    ],
    [
      `Negative feedback highlights <b>${negWords}</b>.`,
      `Users are facing challenges impacting overall performance.`,
      `Addressing these problems can improve customer trust.`
    ]
  ];

  const neutralSet = [
    [
      `Customers mentioned <b>${neuWords}</b> in feedback.`,
      `This shows an average or balanced user experience.`,
      `There is clear scope to improve and impress users.`
    ],
    [
      `Neutral opinions focus on <b>${neuWords}</b>.`,
      `Users neither strongly like nor dislike the product.`,
      `Enhancements can convert them into satisfied customers.`
    ]
  ];

  // =========================
  // RANDOM PICK
  // =========================

  const randomPick = (arr) => arr[Math.floor(Math.random() * arr.length)];

  const posLines = randomPick(positiveSet);
  const negLines = randomPick(negativeSet);
  const neuLines = randomPick(neutralSet);

  return `
    <h2>📊 Feedback Analysis Summary</h2>

    <h3>🟢 Positive (${posPct}%)</h3>
    <p>${posLines.join("<br>")}</p>

    <h3>🔴 Negative (${negPct}%)</h3>
    <p>${negLines.join("<br>")}</p>

    <h3>⚪ Neutral (${neuPct}%)</h3>
    <p>${neuLines.join("<br>")}</p>
  `;
}



/* ===== SIDEBAR FIX ===== */

.sidebar {
  width: 220px;
  background: #0f1f3d;
  color: white;
  padding: 20px;
  position: fixed;
  height: 100%;
  transition: 0.3s;
}

.sidebar.collapsed {
  width: 70px;
}

/* hide text */
.sidebar.collapsed span {
  display: none;
}

/* center icons */
.sidebar.collapsed .menu a {
  justify-content: center;
}

/* ===== MAIN ===== */

.main {
  margin-left: 220px;
  padding: 20px;
  transition: 0.3s;
}

.main.expanded {
  margin-left: 70px;
}

/* ===== TOPBAR ===== */

.topbar {
  display: flex;
  align-items: center;
  gap: 15px;
  background: white;
  padding: 12px 20px;
  border-radius: 10px;
  margin-bottom: 20px;
}

/* ===== MENU BUTTON ===== */

#menuToggle {
  font-size: 22px;
  background: #2563eb;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 8px;
  cursor: pointer;
}

#menuToggle:hover {
  background: #1e40af;
}

