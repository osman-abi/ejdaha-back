<template>
  <div class="division">
      <input type="text" v-model="search"  id="searchList" placeholder="Search...">
    <table class="table" border="3">
        <thead id="thead">
      <tr>
      <th v-for="head in tableHead" :key="head">
        {{head}}
      </th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="j in filterCustomer" :key="j.id">
        <td>
            <router-link :to="'/sifarishi_tamamla/'+j.id">
            {{j.id}}
            </router-link>
        </td> 
        <td>
          <router-link :to="'/sifarishi_tamamla/'+j.id">
            {{j.name}}
          </router-link>
        </td>
        <td>
          <router-link :to="'/sifarishi_tamamla/'+j.id">
            {{j.username}}
          </router-link>
        </td>
        <td>
            <router-link :to="'/sifarishi_tamamla/'+j.id">
            {{j.website}}
            </router-link>
        </td>
        <td>
            <router-link :to="'/sifarishi_tamamla/'+j.id">
            {{j.address.street}}
            </router-link>
        </td>

      </tr>
      </tbody>
    </table>
  
  </div>
</template>

<script>
export default {
    data() {
      return {
        tableHead:["No:","Ad","Soyad","Sifarish","Location"],
        datas: [],
        search:''
      }
    },
    created (){
        fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => response.json())
        .then(data => {
            for (let index = 0; index < data.length; index++) {
                this.datas = data                
            }
        })
    },
    computed:{
        filterCustomer:function(){
            return this.datas.filter((customer)=>{
                return customer.name.match(this.search)
            })
        }
    }
}
</script>

<style scoped>
.division{

  text-align: center;
  
}

tr:nth-child(even){
  background:  #4b4276 !important
}


  .searchBar{
    width: 90%;
  }

  td{
      text-align: center;
  }

  #searchList{
      width: 70%;
  }

  #thead{
      background-color: #4b4276 !important;
    

}


  
</style>
