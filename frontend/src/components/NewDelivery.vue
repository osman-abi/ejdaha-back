<template>
   <div>
     
     {{customer.id}} <br> {{customer.name}} <br> {{customer.address.street}} <br> {{customer.website}} <br> {{customer.username}}
     
   </div>
</template>


<script>
export default {  
  data(){
    return{
      id: this.$route.params.id,
      customer: {},
      table_head:['No','Ad',"Soyad",'Sifarish']
    }
  },
  created(){

        fetch('https://jsonplaceholder.typicode.com/users/'+this.id)
        .then(response => response.json())
        .then(data => {
          this.customer = data
          console.log(data.address)
          })
  }
}
</script>

<style scoped>
  div{
    margin-left: 20px;
  }
</style>