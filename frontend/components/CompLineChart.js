import { Line, mixins } from "vue-chartjs";
const { reactiveProp } = mixins;

export default {
  extends: Line,
  mixins: [reactiveProp],
  props: ["options", "text"],

  mounted() {
    this.renderChart(this.chartData, {
      responsive: true,
      title: {
        display: true,
        text: this.text,
      },
      tooltips: {
        enabled: true,
        callbacks: {
          label(tooltipItems, data) {
            const size = ["b", "kbps", "mbps"];

            const i = parseInt(
              Math.floor(Math.log(tooltipItems.yLabel) / Math.log(1024))
            );
            let label = data.datasets[tooltipItems.datasetIndex].label + ": ";

            label +=
              (tooltipItems.yLabel / Math.pow(1024, i)).toFixed(2) +
              " " +
              size[i];
            return label;
          },
        },
      },
      legend: {
        display: false,
      },
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              callback(bytes) {
                const size = ["b", "kbps", "mbps"];
                if (bytes === 0) {
                  return "0 b";
                }
                const i = parseInt(
                  Math.floor(Math.log(bytes) / Math.log(1024)),
                  10
                );
                return (bytes / Math.pow(1024, i)).toFixed(2) + " " + size[i];
              },
            },
          },
        ],
      },
    });
  },
};
