
new Chart(document.getElementById("pieChart"), {
  type: "pie",
  data: {
    labels: ["Positive", "Negative", "Neutral"],
    datasets: [{
      data: [pos, neg, neu],
      backgroundColor: [
        "#0d7941",
        "#710b0b",
        "#2f3438b0"
      ],
      borderColor: "#ffffff",
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "bottom",
        labels: {
          boxWidth: 14,
          padding: 15
        }
      },
      tooltip: {
        callbacks: {
          label: function(context) {
            const total = context.dataset.data.reduce((a, b) => a + b, 0);
            const value = context.raw;
            const percent = ((value / total) * 100).toFixed(2);
            return `${context.label}: ${percent}%`;
          }
        }
      }
    }
  }
});
