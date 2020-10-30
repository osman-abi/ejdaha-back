<template>
<div class="card">
    <h5 class="card-header info-color white-text text-center py-4">
        <strong>Sign up</strong>
    </h5>
    <div class="card-body px-lg-5 pt-0">
        <form class="text-center" style="color: #757575;" action="#!">
            <div class="form-row">
                <div class="col">
                    <div class="md-form">
                        <input type="text" id="materialRegisterFormFirstName" class="form-control">
                        <label for="materialRegisterFormFirstName">First name</label>
                    </div>
                </div>
                <div class="col">
                    <div class="md-form">
                        <input type="email" id="materialRegisterFormLastName" class="form-control">
                        <label for="materialRegisterFormLastName">Last name</label>
                    </div>
                </div>
            </div>

            <div class="md-form mt-0">
                <input type="email" id="materialRegisterFormEmail" class="form-control">
                <label for="materialRegisterFormEmail">E-mail</label>
            </div>
            <div class="md-form">
                <input type="password" id="materialRegisterFormPassword" class="form-control" aria-describedby="materialRegisterFormPasswordHelpBlock">
                <label for="materialRegisterFormPassword">Password</label>
                <small id="materialRegisterFormPasswordHelpBlock" class="form-text text-muted mb-4">
                    At least 8 characters and 1 digit
                </small>
            </div>

             <div class="md-form">
                <input type="password" id="materialRegisterFormPassword" class="form-control" aria-describedby="materialRegisterFormPasswordHelpBlock">
                <label for="materialRegisterFormPassword">Confirm Password</label>
                <small id="materialRegisterFormPasswordHelpBlock" class="form-text text-muted mb-4">
                    At least 8 characters and 1 digit
                </small>
            </div>

            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="materialRegisterFormNewsletter">
                <label class="form-check-label" for="materialRegisterFormNewsletter">Subscribe to our newsletter</label>
            </div>
            <button class="btn btn-outline-info btn-rounded btn-block my-4 waves-effect z-depth-0" type="submit">Sign in</button>
            <p>or sign up with:</p>
              <a href="#" class="mx-2" role="button"><i class="fab fa-facebook-f light-blue-text"></i></a>
              <a href="#" class="mx-2" role="button"><i class="fab fa-twitter light-blue-text"></i></a>
              <a href="#" class="mx-2" role="button"><i class="fab fa-linkedin-in light-blue-text"></i></a>
              <a href="#" class="mx-2" role="button"><i class="fab fa-google"></i></a>
            <p>By clicking</p>
            <em>Sign up</em> you agree to our
            <a href="" target="_blank">terms of service</a>

        </form>
     </div>

</div>

</template>

<script>
export default {

}
</script>

<style>

.card-header{
    background-color: #4b4276;
    
}
.btn-outline-info{
    background-color: #4b4276;
    color: #4b4276;
}

.card{
    font-family: 'Raleway', sans-serif;
}


</style>