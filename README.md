html file


<!DOCTYPE html>
<html>
<head>
  <title>Insights</title>
  <link rel="stylesheet" href="style.css">

<body>
<style>

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
</style>
</head>



<div class="layout">

  <!-- ===== SIDEBAR ===== -->
  <aside class="sidebar">

    <div class="brand">
      <span>Sentiment Analyzer </span>
    </div>

    <nav class="menu">

       <a href="index.html">
        🏠 Home
      </a>

      <a href="analyze.html">
        🧠 Analyze Review
      </a>

      <a href="upload.html">
        ⬆ Upload CSV
      </a>

      <a href="dashboard.html" >
        📊 Dashboard
      </a>

    
      <a href="insights.html" class="active">
        📈 Insights
      </a>


     

    </nav>

  </aside>

  <!-- ===== MAIN AREA ===== -->
  <div class="main">

    <!-- TOP BAR -->
    <header class="topbar">
      <h2>Insights</h2>

      <div class="user">
      <span class="avatar"></span>
      </div>
    </header>


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

<script>

function loadInsights(){

const data = JSON.parse(localStorage.getItem("chartData"));

if(!data){

  return;
}

// safe getter
const getVal = (val, def) => (val !== undefined ? val : def);

// set values
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

window.onload = loadInsights;

</script>

</body>
</html>







Css file

body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: #f5f7fa;
}












.navbar {
  display: flex;
  justify-content: space-between;
  padding: 15px 40px;
  background: white;
  border-bottom: 1px solid #ddd;
}

.logo { margin-left: 20px; font-weight: bold; font-size: 20px; }
/* ===== LOGO STYLE ===== */

.topbar h2 {
  font-size: 22px;
  font-weight: bold;
  color: #446776;
  position: relative;

  /* Smooth animation */
  animation: bubbleFloat 4s ease-in-out infinite;

  /* Soft glow */
  text-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
}

/* ===== BUBBLE FLOAT ANIMATION ===== */

@keyframes bubbleFloat {

  0% {
    transform: translateY(0px) scale(1);
  }

  25% {
    transform: translateY(-4px) scale(1.02);
  }

  50% {
    transform: translateY(-8px) scale(1.04);
  }

  75% {
    transform: translateY(-4px) scale(1.02);
  }

  100% {
    transform: translateY(0px) scale(1);
  }
}

.logo::after {
  content: "";
  position: absolute;
  top: -6px;
  left: -6px;
  right: -6px;
  bottom: -6px;

  border-radius: 50%;
  background: radial-gradient(
    circle at top left,
    rgba(255,255,255,0.8),
    transparent 60%
  );

  opacity: 0.4;
  pointer-events: none;
}


.nav-links a {
  margin-left: 20px;
  text-decoration: none;
  color: #333;
}
.logo {
  display: flex;
  align-items:left;
  margin-right: 50px; /* spacing from menu */
}



/* ===== LAYOUT ===== */

.layout {
  display: flex;
  min-height: 100vh;
  background: #f5f7fb;
  font-family: "Segoe UI", sans-serif;
}

/* ===== SIDEBAR ===== */

.sidebar {
  width: 220px;
  background: #0f1f3d;
  color: white;
  padding:20px;
}

.brand {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 30px;
}

/* ===== MENU ===== */

.menu h4 {
  margin: 20px 0 10px;
  font-size: 13px;
  color: #9aa8c7;
}

.menu a {
  display: block;
  padding: 12px;
  color: #dbe2f1;
  text-decoration: none;
  border-radius: 10px;
  margin-bottom: 6px;
  transition: 0.2s;
}

.menu a{
display:flex;
align-items:center;
padding:12px 14px;
gap:10px;
}

/*
.menu a:hover,
.menu a.active {
  
}
*/

/* ===== MAIN AREA ===== */

.main {
  flex: 1;
  padding: 20px 30px;
}

/* ===== TOP BAR ===== */

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

/*
.user {
  display: flex;
  align-items: center;
  gap: 15px;
}

.avatar {
  background: #2563eb;
  color: white;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

 */

.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px,1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.metric-card {
  background: white;
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

.metric-card h3 {
  margin: 0;
  font-size: 16px;
  color: #6b7280;
}

.metric-card .value {
  font-size: 28px;
  font-weight: bold;
  margin-top: 8px;
  color: #111827;
}














nav{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}
nav ul li{
  display: inline-block;
  list-style: none;
  margin :10px 20px;
}
nav ul li a{
 color: #000000;
  text-decoration:none;
  font-size:18px;
 position: relative;
}

nav ul li a::after{
content:'' ;
width: 0;
height: 3px;
background: #42bdea;
  
 position: absolute;
 left: 0;
 bottom: -6px;
 transition: 0.4s;
}
nav ul li a:hover::after{
  width: 70px;
}





/* RESULT CARD */

#result {
  margin-top: 25px;
  display: block;
}

.result-card {
  background: white;
  padding: 20px 30px;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
  font-size: 18px;
  display: inline-block;
}

/* ===== INSIGHTS PAGE GRID ===== */

.metrics-grid {
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
  padding: 40px 20px;
}

/* ===== CARD STYLE ===== */

.feature-grid{
    display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
  padding: 40px 20px;

}
.card {
  width: 260px;
  padding: 25px;
  border-radius: 18px;

  /* Glass effect */
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(8px);

  box-shadow: 0 12px 30px rgba(0,0,0,0.15);

  text-align: center;
  transition: all 0.35s ease;
  position: relative;
  overflow: hidden;
}

/* ===== TOP ACCENT LINE ===== */

.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 6px;
  width: 100%;
  background: linear-gradient(90deg, #2563eb, #44917e);
}

/* ===== TITLE ===== */
.features h2 {
  text-align: center;
}
/* ===== CARD BASE ===== */

.card {
  width: 260px;
  padding: 25px;
  border-radius: 18px;

  /* Colorful gradient background */
  background: linear-gradient(135deg, #e0ecff, #f0fff4);

  /* Glass + shadow */
  backdrop-filter: blur(8px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.15);

  text-align: center;
  position: relative;
  overflow: hidden;

  /* Floating animation */
  animation: floatCard 5s ease-in-out infinite;

  transition: all 0.35s ease;
}

/* ===== TOP COLOR STRIP ===== */

.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 6px;
  width: 100%;
  background: linear-gradient(90deg, #456bbe, #678e76, #5c412b);
}

/* ===== FLOATING ANIMATION ===== */

@keyframes floatCard {
  0%   { transform: translateY(0px); }
  50%  { transform: translateY(-15px); }
  100% { transform: translateY(px); }
}

/* ===== TITLE ===== */

.card h3 {
  margin-top: 10px;
  font-size: 20px;
  color: #0d0f11;
}

/* ===== TEXT ===== */

.card p {
  margin: 8px 0;
  font-size: 16px;
  color: #374151;
}

/* ===== KEEP YOUR HOVER EFFECT ===== */

.card:hover {
  transform: translateY(-10px) scale(1.03);
  box-shadow: 0 18px 40px rgba(0,0,0,0.2);
}

/* ===== ACCURACY HIGHLIGHT ===== */

.card p:first-of-type {
  font-weight: bold;
  color: #000000;
}

/* ===== F1 SCORE STYLE ===== */

.card p:last-of-type {
  color: #1d6ab2;
  font-weight: 500;
}


.report-section{
margin-top:30px;
text-align:center;
}

.download-btn{

background:linear-gradient(135deg,#2563eb,#1e40af);
color:white;
border:none;
padding:14px 24px;
font-size:16px;
border-radius:10px;
cursor:pointer;
display:inline-flex;
align-items:center;
gap:10px;

box-shadow:0 8px 20px rgba(0,0,0,0.15);
transition:all .3s ease;

}

.download-btn:hover{

transform:translateY(-3px);
box-shadow:0 12px 25px rgba(0,0,0,0.2);

background:linear-gradient(135deg,#1e40af,#000);

}

.download-btn .icon{
font-size:18px;
}

/* ===== PAGE BACKGROUND (OPTIONAL) ===== */
/*
body {
  background: linear-gradient(135deg, #eef2f7, #dbeafe);
  font-family: "Segoe UI", sans-serif;
}
/*








/* Sentiment colors */
.positive { color: green; font-weight: bold; }
.negative { color: red; font-weight: bold; }
.neutral  { color: rgb(110, 95, 66); font-weight: bold; }

.nav-links .active {
  color: #2563eb;
  border-bottom: 2px solid #2563eb;
}

.hero {
  text-align: center;
  padding: 80px;
}

/* ===== NAVBAR ===== */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 40px;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.logo {
  font-weight: bold;
  font-size: 20px;
}

.nav-links a {
  margin-left: 25px;
  text-decoration: none;
  color: #333;
  font-weight: 500;
  position: relative;
}

/* Active tab */
.nav-links .active {
  color: #2563eb;
  border-bottom: 2px solid #2563eb;
}

/* Hover animation */
.nav-links a:hover {
  color: #2563eb;
}

.page {
  text-align: center;
  padding: 60px;
}

textarea {
  width: 60%;
  height: 150px;
  padding: 10px;
}

button {
  padding: 12px 25px;
  background: #2563eb;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
/*
.result-box {
  margin-top: 20px;
  background: white;
  padding: 20px;
  display: inline-block;
  border-radius: 8px;
}
*/

/* ===== BACKGROUND ===== */
body {
  margin: 0;
  font-family: "Segoe UI", sans-serif;
  background: linear-gradient(135deg, #eef2f7, #dfe9f3);
}

/* ===== NAVBAR ===== */
.navbar {
  padding: 15px 40px;
  background: white;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  font-weight: bold;
  font-size: 20px;
}

/* ===== DASHBOARD LAYOUT ===== */
.dashboard-container {
  text-align: center;
  padding: 40px;
}

.dash-title {
  margin-bottom: 20px;
}

/* ===== SUMMARY CARD ===== */
.summary-card {
  display: inline-block;
  padding: 20px 30px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  margin-bottom: 30px;
  font-size: 18px;
  animation: fadeIn 1s ease;
}

/* ===== CHART GRID ===== */








.chart-container{
display:grid;
grid-template-columns:1fr 1fr;
gap:25px;
}

.chart-card{
height:320px;
}

.chart-card canvas{
width:100% !important;
height:280px !important;
}

#gaugeChart{
height:280px!important;
}









/*
.charts-grid {
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
}

/* ===== CHART CARD ===== */


/* INSIGHTS BOX */
.insights-box {
  margin-top: 30px;
  background: white;
  padding: 25px;
  border-radius: 14px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.12);
  text-align: left;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

.insights-box h3 {
  margin-top: 0;
}

/* ===== HERO TEXT COLORS ===== */

.ml {
  color: #2563eb;   /* Blue */
  font-weight: 700;
}

.cf {
  color: #16a34a;   /* Green */
  font-weight: 700;
}

.nlp {
  color: #233540;   /* Orange */
  font-weight: 700;
}

.insight {
  color: #552b48;   /* Purple */
  font-weight: 700;
}

/* ===== PAGE WRAPPER ===== */
.page {
  text-align: center;
  margin-top: 40px;
}

/* ===== UPLOAD BOX ===== */
.upload-box {
  background: white;
  padding: 40px;
  border-radius: 20px;
  width: 350px;
  margin: 20px auto;
  box-shadow: 0 10px 30px rgba(0,0,0,0.12);
  transition: 0.3s ease;
  border: 2px dashed #2563eb;
}

.upload-box:hover {
  transform: translateY(-6px);
  box-shadow: 0 18px 40px rgba(0,0,0,0.18);
}

/* ===== FILE INPUT ===== */
.upload-box input {
  margin-top: 10px;
}

/* ===== BUTTON ===== */
button {
  padding: 12px 24px;
  border-radius: 12px;
  border: none;
  background: linear-gradient(135deg, #2563eb, #4CAF50);
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: 0.3s ease;
}

button:hover {
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(0,0,0,0.2);
}

/* ===== UPLOAD MESSAGE ===== */
.upload-message {
  margin-top: 25px;
  font-size: 18px;
  font-weight: 500;
  animation: fadeIn 0.5s ease-in-out;
}

.upload-message img {
  width: 60px;
  margin-top: 10px;
}

/* SUCCESS */
.success {
  color: #16a34a;
}

/* ERROR */
.error {
  color: #dc2626;
}

/* ANIMATION */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

