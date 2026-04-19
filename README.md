


/* ===== SIDEBAR TOGGLE ===== */

.sidebar {
  width: 220px;
  transition: all 0.3s ease;
}

/* collapsed */
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

/* main shift */
.main {
  margin-left: 220px;
  transition: all 0.3s ease;
}

.main.expanded {
  margin-left: 70px;
}

/* toggle button */
#menuToggle {
  font-size: 22px;
  background: none;
  border: none;
  cursor: pointer;
  margin-right: 10px;
}






<!DOCTYPE html>
<html>
<head>
  <title>Insights</title>
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

      <a href="insights.html" class="active">
        📈 <span>Insights</span>
      </a>

    </nav>

  </aside>

  <!-- ===== MAIN AREA ===== -->
  <div class="main">

    <!-- TOP BAR -->
    <header class="topbar">
      <button id="menuToggle">☰</button>
      <h2>Insights</h2>
    </header>

    <!-- PAGE -->
    <div class="page">
      <h2>Insights</h2>

      <div class="metrics-grid">

        <div class="card">
          <h3>Logistic Regression</h3>
          <p>Accuracy: <span id="lrAcc">--</span></p>
          <p>Macro F1: <span id="lrF1">--</span></p>
        </div>

        <div class="card">
          <h3>Linear SVM</h3>
          <p>Accuracy: <span id="svmAcc">--</span></p>
          <p>Macro F1: <span id="svmF1">--</span></p>
        </div>

        <div class="card">
          <h3>Random Forest</h3>
          <p>Accuracy: <span id="rfAcc">--</span></p>
          <p>Macro F1: <span id="rfF1">--</span></p>
        </div>

      </div>
    </div>

  </div>

</div>

<!-- ================= JS ================= -->
<script>

// ================= LOAD INSIGHTS =================
function loadInsights(){

  const data = JSON.parse(localStorage.getItem("chartData"));

  if(!data) return;

  const getVal = (val, def) => (val !== undefined ? val : def);

  document.getElementById("lrAcc").innerText =
    getVal(data.logistic_accuracy, "--") + "%";

  document.getElementById("lrF1").innerText =
    getVal(data.logistic_f1, "--");

  document.getElementById("svmAcc").innerText =
    getVal(data.svm_accuracy, "--") + "%";

  document.getElementById("svmF1").innerText =
    getVal(data.svm_f1, "--");

  document.getElementById("rfAcc").innerText =
    getVal(data.rf_accuracy, "--") + "%";

  document.getElementById("rfF1").innerText =
    getVal(data.rf_f1, "--");
}


// ================= SIDEBAR TOGGLE =================
document.addEventListener("DOMContentLoaded", function () {

  loadInsights();

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
