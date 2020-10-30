<template>
<div class = "row map">
    <l-map :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
      <l-marker :lat-lng="marker"></l-marker>
        <l-marker :lat-lng="markers"></l-marker>
         <l-marker :lat-lng="markerd"></l-marker>
          <l-marker :lat-lng="markerb"></l-marker>
          <l-marker :lat-lng="markerg"></l-marker>
          <l-marker :lat-lng="markerl"></l-marker>
          <l-marker :lat-lng="markerz"></l-marker>
          <l-marker :lat-lng="markerx"></l-marker>
    </l-map>
   
</div>

</template>


<script>
    import L from 'leaflet';
    import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
    export default{
        name: "Map",
        data: function(){
            return{
                 zoom:10,
                center: L.latLng(40.409264, 49.867092),
                url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
                attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                marker: L.latLng(40.409264, 49.867092),
                markers:L.latLng(40.58972, 49.66861),
                 markerd:L.latLng(40.4444, 49.80566),
                  markerb:L.latLng(40.44808, 49.75502),
                  markerg: L.latLng(40.3256, 49.73376),
                  markerl:L.latLng(40.3256, 49.73376),
                  markerz:L.latLng(40.39667, 49.97361),
                  markerx:L.latLng(40.51903, 50.11438)
               
            }
        },
        components: {
        LMap,
        LTileLayer,
        LMarker,
        }
       
    }
</script>

<style scoped>
.map{
    height: 50vh;
    
    
}

</style>