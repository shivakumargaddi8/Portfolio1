// PIE CHART
 new Chart(document.getElementById("pieChart"), {
  type: "doughnut",
  data: {
    labels: [" Positive ", " Negative", " Neutral"],
    datasets: [{
      data: [pos, neg, neu],
     backgroundColor: [
"#0d7941",
"#710b0b",
"#2f3438b0"
],
      borderWidth: 6
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: "65%",
    plugins: {
      legend: {
        position: "bottom"
      }
    }
  },
  plugins: [{
    id: "centerText",
    afterDraw(chart) {
      const {ctx} = chart;

      ctx.save();
      ctx.font = "bold 28px Poppins";
      ctx.fillStyle = "#1f2937";
      ctx.textAlign = "center";

      ctx.fillText(confidence + "%", chart.width/2, chart.height/2);

      ctx.font = "14px Poppins";
      ctx.fillStyle = "#9ca3af";
      ctx.fillText("Sentiment Score", chart.width/2, chart.height/2 + 25);

      ctx.restore();
    }
  }]
});

};
