<template>
<div class="login">
  <form class="text-center border border-light p-5" action="#!">

    <p class="h4 mb-4">Log in</p>

  
    <input type="email" id="defaultLoginFormEmail" class="form-control mb-4" placeholder="E-mail">

    <input type="password" id="defaultLoginFormPassword" class="form-control mb-4" placeholder="Password">

    <div class="d-flex justify-content-around">
        <div>
           
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="defaultLoginFormRemember">
                <label class="custom-control-label" for="defaultLoginFormRemember">Remember me</label>
            </div>
        </div>
        <div>
            <a href="">Forgot password?</a>
        </div>
    </div>
    <button class="btn btn-info btn-block my-4" type="submit">Sign in</button>
    <p>Not a member? 
        <router-link to="/register">Register</router-link>
    </p>

    <p>or sign in with:</p>

    

</form>
</div>


</template>

<script>


export default {
 
}
</script>

<style scoped>
.login {
    margin-top: auto;
    
}

.btn-info{
  background-color: #4b4276 !important;
  
}


</style>