
<!DOCTYPE html>
<html>
<head>
  <title>Upload CSV</title>
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
      <a href="analyze.html">🧠 <span>Analyze Review</span></a>
      <a href="upload.html" class="active">⬆ <span>Upload CSV</span></a>
      <a href="dashboard.html">📊 <span>Dashboard</span></a>
      <a href="insights.html">📈 <span>Insights</span></a>

    </nav>

  </aside>

  <!-- ===== MAIN AREA ===== -->
  <div class="main">

    <!-- ===== TOP BAR ===== -->
    <header class="topbar">
      <button id="menuToggle">☰</button>
      <h2>Upload CSV</h2>
    </header>

    <!-- ===== PAGE ===== -->
    <div class="page">

      <h2>Upload CSV File</h2>

      <div class="upload-box">
        <input type="file" id="csvFile" accept=".csv">
      </div>

      <button onclick="uploadCSV()">Upload and Analyze</button>

      <div id="uploadMessage" class="upload-message"></div>

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

