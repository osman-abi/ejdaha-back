<template>
  <div id="app">
    <Navbar id="nav" />
    
    <router-view id="rota"></router-view>
      
     
      
      
   
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'



export default {
  name: 'App',
  components: {
    Navbar
  
  }

   
    
    
  

}
</script>

<style>
#app {
  font-family: 'Commissioner', sans-serif;
  display: flex;

}

#nav{
  flex: 1;
}

#nav+#rota{
  flex: 7;
}
</style>
