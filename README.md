

<!DOCTYPE html>
<html>
<head>
  <title>Page Name</title>
  <link rel="stylesheet" href="style.css">

  <!-- Charts (keep only where needed) -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>

<body>

<div class="layout">

  <!-- ================= SIDEBAR ================= -->
  <aside class="sidebar">

    <div class="brand">
      🎓 <span>Sentiment Analyzer</span>
    </div>

    <nav class="menu">

      <a href="index.html">
        🏠 <span>Home</span>
      </a>

      <a href="analyze.html">
        🧠 <span>Analyze Review</span>
      </a>

      <a href="upload.html">
        ⬆ <span>Upload CSV</span>
      </a>

      <a href="dashboard.html">
        📊 <span>Dashboard</span>
      </a>

      <a href="insights.html">
        📈 <span>Insights</span>
      </a>

    </nav>

  </aside>

  <!-- ================= MAIN ================= -->
  <div class="main">

    <!-- TOPBAR -->
    <header class="topbar">
      <button id="menuToggle">☰</button>
      <h2 id="pageTitle">Page Name</h2>
    </header>

    <!-- ================= PAGE CONTENT ================= -->
    <div class="page">

      <!-- 🔽 Replace this section per page -->
      <h2>Welcome</h2>
      <p>Your content goes here...</p>

    </div>

  </div>

</div>

<!-- ================= SCRIPT ================= -->
<script src="script.js"></script>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const toggleBtn = document.getElementById("menuToggle");
  const sidebar = document.querySelector(".sidebar");
  const main = document.querySelector(".main");

  toggleBtn.addEventListener("click", () => {
    sidebar.classList.toggle("collapsed");
    main.classList.toggle("expanded");

    localStorage.setItem("sidebarState", sidebar.classList.contains("collapsed"));
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



.sidebar.collapsed {
  width: 70px;
}

.sidebar.collapsed span {
  display: none;
}

.main {
  margin-left: 220px;
  transition: 0.3s;
}

.main.expanded {
  margin-left: 70px;
}







