<!DOCTYPE html>
<html>
<head>
<title>Sentiment Dashboard</title>

<link rel="stylesheet" href="style.css">

<!-- ChartJS -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>

/* Layout */
body{
margin:0;
font-family:Arial, sans-serif;
background:#f3f4f6;
}

.layout{
display:flex;
min-height:100vh;
}

/* Sidebar */

.sidebar{
width:220px;
background:#1e293b;
color:white;
padding:20px;
}


.brand{
font-size:22px;
font-weight:bold;
margin-bottom:30px;
}

.menu a{
display:block;
color:white;
text-decoration:none;
padding:10px;
margin-bottom:8px;
border-radius:6px;
}

.menu a:hover{
background:#334155;
}

.menu a.active{
background:#2563eb;
}

/* Main content */

.main{
flex:1;
padding:25px;
}

/* Topbar */

.topbar{
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:25px;
}



/* Summary card */

.summary-card{
background:white;
padding:20px;
border-radius:10px;
margin-bottom:25px;
box-shadow:0 4px 10px rgba(0,0,0,0.05);
font-size:16px;
}

/* Charts */

.chart-container{
display:grid;
grid-template-columns:1fr 1fr;
gap:25px;
}

.chart-card{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0 8px 20px rgba(0,0,0,0.08);
height:320px;
}

.chart-card canvas{
width:100%!important;
height:250px!important;
}

/* Full width card */

.full{
grid-column:1/3;
}

/* Insights */

.insights-box{
background:white;
padding:20px;
border-radius:10px;
margin-top:30px;
box-shadow:0 4px 10px rgba(0,0,0,0.05);
}

.dash-title{
margin-bottom:20px;
}

</style>

</head>

<body>

<div class="layout">

<!-- Sidebar -->

<aside class="sidebar">

<div class="brand">
Sentiment Analyzer
</div>

<nav class="menu">

<a href="index.html">🏠 Home</a>

<a href="analyze.html">🧠 Analyze Review</a>

<a href="upload.html">⬆ Upload CSV</a>

<a href="dashboard.html" class="active">📊 Dashboard</a>

<a href="insights.html">📈 Insights</a>

</nav>

</aside>


<!-- Main -->

<div class="main">

<header class="topbar">

<h2>Dashboard</h2>

<div class="avatar"></div>

</header>


<h1 class="dash-title">Sentiment Analysis Dashboard</h1>

<!-- Summary -->

<div id="summary" class="summary-card"></div>


<!-- Charts -->

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

<div class="report-section">

<button class="download-btn" onclick="downloadReport()">

<span class="icon">⬇</span>
Download Sentiment Report

</button>

</div>


<!-- Insights -->

<div id="insights" class="insights-box"></div>

</div>

</div>


<!-- Script -->
 <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<script src="script.js"></script>

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

