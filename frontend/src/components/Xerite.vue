<template>

   
<div>
    <p v-show = "error">{{error}}</p>

  <b-form-input v-model="data" placeholder="Enter your address" id = "autocomplete"></b-form-input>
  <b-button variant="danger"  v-on:click="locatorButtonPressed">Button</b-button>
  
  <section id = "map"></section>
</div>

</template>


<script>
import axios from 'axios'
export default{
    data(){
        return{
            data:"",
            error:""
                }
    },
        mounted(){
            new google.maps.places.Autocomplete(
                document.getElementById("autocomplete"),
    {
                    bounds:new google.maps.LatLngBounds(
                        new google.maps.LatLng(40.37767, 49.89201)
                    )
                }
            )
            

    },

    methods:{
        locatorButtonPressed(){
            if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(position => {
            this.getAddressFrom(position.coords.latitude,position.coords.longitude);
            this.showUserLocationOnTheMap(position.coords.latitude,position.coords.longitude);
                        
    },
error =>{
        this.error = error.message
                        

    }
)
    }else{
        this.error = error.message
                    
    }
},
getAddressFrom(lat,long){
axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+ lat + 
    ","
    + long 
    + "&key = yourkey")
.then(response => {
if(response.data.error_message){
this.error = response.data.error_message
                        
}else{
    this.address = response.data.results[0].formatted_address
                        
}
})
.catch(error =>{
    this.error = error.message
                    
});


},
showUserLocationOnTheMap(latitude,longitude){
    let map = new google.maps.Map(document.getElementById("map"),{
        zoom:15,
        center:new google.maps.LatLng(latitude,longitude),
        mapTypeId: google.maps.MapTypeId.ROADMAP
})
    new google.maps.Marker({
    position: new google.maps.LatLng(latitude,longitude),
        map:map
})

    }
}

}
</script>

<style scoped>

#map{
    height:40vh;
    
}
</style>



