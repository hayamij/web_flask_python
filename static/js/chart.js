// Nhận dữ liệu từ HTML:
const labels = window.chartData.labels;
const values = window.chartData.values;

new Chart(document.getElementById("chart"), {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'Số lượng sản phẩm',
            data: values
        }]
    }
});
