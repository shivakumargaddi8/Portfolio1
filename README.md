

<!DOCTYPE html>
<html>
<head>
  <title>Sentiment Analyzer</title>
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

      <a href="index.html" class="active">🏠 <span>Home</span></a>
      <a href="analyze.html">🧠 <span>Analyze Review</span></a>
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
      <h2>Home</h2>
    </header>

    <!-- ===== HERO ===== -->
    <div class="hero">

      <h1>
        <span class="ml">Machine Learning</span>–Enabled
        <span class="cf">Customer Feedback</span> Analysis
      </h1>

      <p>
        Analyze customer reviews using
        <span class="nlp">NLP</span> &
        <span class="ml">ML</span> to gain
        <span class="insight">actionable insights</span>.
      </p>

      <button onclick="location.href='analyze.html'">
        Analyze Review
      </button>

      <button onclick="location.href='upload.html'">
        Upload CSV
      </button>

    </div>

    <!-- ===== FEATURES ===== -->
    <div class="features">

      <h2>Features</h2>

      <div class="feature-grid">

        <div class="card">
          <h3>⚡ Real-time Analysis</h3>
          <p>Analyze feedback instantly.</p>
        </div>

        <div class="card">
          <h3>📊 Bulk Processing</h3>
          <p>Upload CSV files.</p>
        </div>

        <div class="card">
          <h3>📈 Detailed Insights</h3>
          <p>Comprehensive recommendations.</p>
        </div>

        <div class="card">
          <h3>🎯 High Accuracy</h3>
          <p>Advanced ML models.</p>
        </div>

      </div>

    </div>

  </div>

</div>

<!-- ===== SIDEBAR SCRIPT ===== -->
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

  // restore state
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

