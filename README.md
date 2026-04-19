<!DOCTYPE html>
<html>
<head>
  <title>Sentiment Analyzer</title>
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

<a href="index.html" class="active">🏠 Home</a>

<a href="analyze.html" >🧠 Analyze Review</a>

<a href="upload.html" >⬆ Upload CSV</a>

<a href="dashboard.html" >📊 Dashboard</a>

<a href="insights.html" >📈 Insights</a>

    </nav>

  </aside>

  <!-- ===== MAIN AREA ===== -->
  <div class="main">

    <!-- TOP BAR -->
      <header class="topbar">
      <h2>Home</h2>

      <div class="user">
      <span class="avatar"></span>
      </div>
    </header>






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

  </div> <!-- main -->
</div> <!-- layout -->

</body>
</html>

