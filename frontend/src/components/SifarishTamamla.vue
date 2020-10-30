<template>
  <div>
    
      <div class="container m-auto py-5">
          <div class="row">
              <div class="col">
              <table class="font" id="customer">
          
          <tr>
              <th  v-for="data in table_head" :key="data">{{data}}</th>
          </tr>
          <tr>
             <td> {{customer.id}} </td>
             <td> {{customer.name}} </td>
             <td> {{customer.username}} </td>
             <td>{{customer.website}}</td>
             <td> {{customer.address.city}} </td> 
          </tr>
      </table>
      </div>
      <div class="col">
         <table class="font col" id="courier">
          <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Surname</th>
              <th>Adress</th>
              <th>Price</th>
          </tr>
          <tr>
              <td>1</td>
              <td>Fabiden</td>
              <td>LeBlanc</td>
              <td>Fabiden@gmail.com</td>
              <td>1500$</td>
          </tr>           
      </table>
      </div>
          </div>

      </div>
      <router-link to='/preview'><button id="submit_button"> Sifarisi Gonder </button></router-link>
    
    <div class="container">
        <Xerite/>
    </div> 
      
  </div>
</template>

<script>
import Xerite from './Xerite.vue'
export default {  
        components: {
            Xerite
           
        },
  data(){
    return{
      id: this.$route.params.id,
      customer: {},
      table_head:['No','Ad',"Soyad",'Sifarish','Location'],
      search: ''
    }},
  
  created(){

        fetch('https://jsonplaceholder.typicode.com/users/'+this.id)
        .then(response => response.json())
        .then(data => {
          this.customer = data
          console.log(data.address.city)
          })
  },
  
}
</script>

<style scoped>

#map{
    margin-top: 20px;
}



#customer {
    /* width: 30%; */
    height: 300px;
    border-collapse: collapse;
    border-spacing: 0;
    border-radius: 15px 15px 0 0;
    box-shadow: 0 20px 10px rgba(32, 32, 32, .3);
    background:  #4b4276;
    text-align: center;
    
    
    
}

#courier {
    /* width: 30%; */
    height: 300px;
    border-collapse: collapse;
    border-spacing: 0;
    border-radius: 15px 15px 0 0;
    box-shadow: 0 20px 10px rgba(32, 32, 32, .3);
    background:  #4b4276;
    text-align: center;
    
}


th,td {
    padding: 12px 15px;
    
}
.font {
    font-family: 'Raleway', sans-serif;
}


#submit_button{
    position: absolute;
    top: 75px;
    right: 20px;
    border-radius: 50%;
    border: 1px solid  #4b4276 !important;
    background-color: #4b4276 !important;
    padding: 20px;
    color: white;
 }

.search_div{
    text-align: center;
    margin: 20px;
     

 }

#searchList{
width: 70%;
    
  }


</style>
