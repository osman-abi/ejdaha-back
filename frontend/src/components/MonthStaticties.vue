<template>
  <div id="statistic_div">
    <div class="row">
 
    <div class="col">
      <p class="w-50  text-center">Month staticties</p>
      <mdb-line-chart id="monthstaticties"
      :data="lineChartData"
      :options="lineChartOptions"
      :width="600"
      :height="300"
      
    ></mdb-line-chart>
    </div>
    
  
    <div class="col text-center">
    <p class="w-60 text-center">Courier staticties</p>
      <CouirerStaticties />
    </div>
    </div>

  </div>
    



</template>

<script>
import CouirerStaticties from './CouirerStaticties.vue'
import { mdbLineChart } from "mdbvue";
export default {
    name: "ChartPage",
    components: {
      mdbLineChart,
      
      CouirerStaticties
    },
    data() {
      return {
        lineChartData: {
          labels: [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July"
          ],
          datasets: [
            {
              label: "My First dataset",
              backgroundColor: "rgba(255, 99, 132, 0.1)",
              borderColor: "rgba(255, 99, 132, 1)",
              borderWidth: 0.7,
              data: [65, 59, 80, 81, 56, 55, 40]
            },
            {
              label: "My Second dataset",
              backgroundColor: "rgba(151,187,205,0.2)",
              borderColor: "rgba(151,187,205,1)",
              borderWidth: 0.8,
              data: [28, 48, 40, 19, 86, 27, 90]
            }
          ]
        },
        lineChartOptions: {
          responsive: false,
          maintainAspectRatio: false,
          scales: {
            xAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                }
              }
            ],
            yAxes: [
              {
                gridLines: {
                  display: true,
                  color: "rgba(0, 0, 0, 0.1)"
                }
              }
            ]
          }
        }
      };
    }
  };
</script>

<style>



#monthstaticties{
  width: 100%;

}

.stat{
  text-align: center;
}






</style>