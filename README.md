
<!DOCTYPE html>
<html>
<head>
  <title>Sentiment Dashboard</title>

  <link rel="stylesheet" href="style.css">

  <!-- ChartJS -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <!-- PDF -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

</head>

<body>

<div class="layout">

  <!-- ===== SIDEBAR ===== -->
  <aside class="sidebar">

    <div class="brand">
      🎓 <span>Sentiment Analyzer</span>
    </div>

    <nav class="menu">
      <a href="index.html">🏠 <span>Home</span></a>
      <a href="analyze.html">🧠 <span>Analyze Review</span></a>
      <a href="upload.html">⬆ <span>Upload CSV</span></a>
      <a href="dashboard.html" class="active">📊 <span>Dashboard</span></a>
      <a href="insights.html">📈 <span>Insights</span></a>
    </nav>

  </aside>

  <!-- ===== MAIN ===== -->
  <div class="main">

    <!-- TOPBAR -->
    <header class="topbar">
      <button id="menuToggle">☰</button>
      <h2>Dashboard</h2>
    </header>

    <h1 class="dash-title">Sentiment Analysis Dashboard</h1>

    <!-- SUMMARY -->
    <div id="summary" class="summary-card"></div>

    <!-- CHARTS -->
    <div class="chart-container">

      <div class="chart-card">
        <h3>Confidence Gauge</h3>
        <canvas id="gaugeChart"></canvas>
      </div>

      <div class="chart-card">
        <h3>Pie Distribution</h3>
        <canvas id="pieChart"></canvas>
      </div>

      <div class="chart-card full">
        <h3>Bar Graph</h3>
        <canvas id="barChart"></canvas>
      </div>

    </div>

    <!-- DOWNLOAD -->
    <div class="report-section">
      <button class="download-btn" onclick="downloadReport()">
        <span class="icon">⬇</span>
        Download Sentiment Report
      </button>
    </div>

    <!-- INSIGHTS -->
    <div id="insights" class="insights-box"></div>

  </div>

</div>

<!-- ===== SCRIPT ===== -->
<script src="script.js"></script>

<script>

// ================= LOAD DASHBOARD =================
window.onload = function () {

  const data = JSON.parse(localStorage.getItem("chartData"));

  if (!data) {
    document.getElementById("summary").innerHTML =
      "No data found. Upload CSV first.";
    return;
  }

  const pos = data.positive;
  const neg = data.negative;
  const neu = data.neutral;

  const total = pos + neg + neu;

  const confidence = Math.round(
    (Math.max(pos, neg, neu) / total) * 100
  );

  // SUMMARY
  document.getElementById("summary").innerHTML =
    `<b>Total Reviews:</b> ${total}<br>
     Positive: ${pos} | Negative: ${neg} | Neutral: ${neu}`;

  // GAUGE
  new Chart(document.getElementById("gaugeChart"), {
    type: "doughnut",
    data: {
      datasets: [{
        data: [confidence, 100 - confidence],
        backgroundColor: ["#2563eb", "#e5e7eb"],
        borderWidth: 0
      }]
    },
    options: {
      rotation: -90,
      circumference: 180,
      cutout: "70%",
      plugins: { legend: { display: false } }
    }
  });

  // PIE
  new Chart(document.getElementById("pieChart"), {
    type: "pie",
    data: {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [{
        data: [pos, neg, neu],
        backgroundColor: ["#16a34a", "#dc2626", "#6b7280"]
      }]
    }
  });

  // BAR
  new Chart(document.getElementById("barChart"), {
    type: "bar",
    data: {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [{
        label: "Reviews",
        data: [pos, neg, neu],
        backgroundColor: ["#16a34a", "#dc2626", "#6b7280"]
      }]
    }
  });

  // INSIGHTS
  document.getElementById("insights").innerHTML =
    generateInsights(data);
};


// ================= SIDEBAR TOGGLE =================
document.addEventListener("DOMContentLoaded", function () {

  const toggleBtn = document.getElementById("menuToggle");
  const sidebar = document.querySelector(".sidebar");
  const main = document.querySelector(".main");

  toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
    main.classList.toggle("expanded");

    localStorage.setItem("sidebarState",
      sidebar.classList.contains("collapsed"));
  });

  const savedState = localStorage.getItem("sidebarState");

  if (savedState === "true") {
    sidebar.classList.add("collapsed");
    main.classList.add("expanded");
  }

});
</script>

</body>
</html>



<!DOCTYPE html>
<html>
<head>
  <title>Analyze Review</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="layout">

  <!-- ===== SIDEBAR ===== -->
  <aside class="sidebar">

    <div class="brand">
      🎓 <span>Sentiment Analyzer</span>
    </div>

    <nav class="menu">

      <a href="index.html">🏠 <span>Home</span></a>
      <a href="analyze.html" class="active">🧠 <span>Analyze Review</span></a>
      <a href="upload.html">⬆ <span>Upload CSV</span></a>
      <a href="dashboard.html">📊 <span>Dashboard</span></a>
      <a href="insights.html">📈 <span>Insights</span></a>

    </nav>

  </aside>

  <!-- ===== MAIN AREA ===== -->
  <div class="main">

    <!-- ===== TOP BAR ===== -->
    <header class="topbar">
      <button id="menuToggle">☰</button>
      <h2>Analyze Review</h2>
    </header>

    <!-- ===== PAGE ===== -->
    <div class="page">

      <h2>Analyze Customer Review</h2>

      <textarea id="review" placeholder="Enter your review here..."></textarea>
      <br><br>

      <button onclick="analyzeReview()">Analyze</button>

      <!-- RESULT -->
      <div id="result"></div>

    </div>

  </div>

</div>

<!-- ===== JS ===== -->
<script src="script.js"></script>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const toggleBtn = document.getElementById("menuToggle");
  const sidebar = document.querySelector(".sidebar");
  const main = document.querySelector(".main");

  toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
    main.classList.toggle("expanded");

    localStorage.setItem("sidebarState",
      sidebar.classList.contains("collapsed"));
  });

  // restore sidebar state
  const savedState = localStorage.getItem("sidebarState");

  if (savedState === "true") {
    sidebar.classList.add("collapsed");
    main.classList.add("expanded");
  }

});
</script>

</body>
</html>











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

