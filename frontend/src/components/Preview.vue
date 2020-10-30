<template>
    <div>
  <table class="table mt-2" border="5">
      <tr>
          <th v-for="data in tableHead" :key="data">
              {{data}}
          </th>
      </tr>
      <tbody>
          <tr>
              <td v-for="data in tableData" :key="data">
                  {{data}}
              </td>
          </tr>
      </tbody>
  </table>
  <button type="button" class="btn btn-primary btn-lg btn-block my-5">Tesdiq et</button>
  </div>
</template>

<script>
export default {
    data(){
        return{
            tableHead:['No','Musterinin adi','Musterinin soyadi','Musterinin sifarisi','Musterinin telefon nomresi','Kuryerin adi','Kuryerin soyadi','Kuryerin telefon nomresi','Location','Km','Saat'],
            tableData:['1','Osman','Mamedov','2doner 1ayran','055 555 55 55','Fuad','Aliyev','055 666 66 66','M.Ecemi mst.','2','23deq']
        }
    }
}
</script>

<style scoped>
.table{
    border-collapse: collapse;
}

td , th{
    border: 1px solid black;
}
div{
    margin-right: 10px;
    margin-top: 200px;
}

.btn-primary{
    background:#4b4276;
}

</style>