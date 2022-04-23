<template>
    <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
    <div>
        <h2>Make</h2> {{make}}
    </div>
    <div>
        <h2>Model</h2> {{model}}
    </div>
    <div>
        <h2>Year</h2> {{year}}
    </div>
    <div>
        <h2>Color</h2> {{color}}
    </div>
    <div>
        <h2>Price</h2> {{price}}
    </div>
    <div>
        <h2>Car Type</h2> {{car_type}}
    </div>
    <div>
        <h2>Transmission</h2> {{transmission}}
    </div>
    <div>
        <h2>Description</h2> {{description}}
    </div>
    <div>
        <h2>Image</h2> <img :src="'/uploads/car_photos/'+ image" alt="car image" width="200" height="200">
    </div>
    <br>
    <div>
        <form class="form" @submit.prevent="addFavorite" id="addFav" method="POST" enctype="multipart/form-data">
            <input type="hidden" id="user_id" class="form-control" name="user_id" :value="user_id">
            <button type="submit" class="btn btn-primary">Add to Favorites</button>
        </form>



    </div>
</template>
<script>
import router from "../router";
import store from '@/main.js';

export default {
    data() {
        return{
            csrfToken: '',
            user_id: sessionStorage.getItem('user_id'),
            errorFlask: [],
            message: '',
            make: '',
            model: '',
            year: '',
            price: '',
            image: '',
            id: '',
            transmission: '',
            color: '',
            car_type: '',
            description: ''
        }
    },
    created() {
        this.getCsrfToken();
        this.getCarDetails();
    },

    methods: {
        addFavorite() {
            let self = this;
            let addFav = document.getElementById('addFav');
            let form_data = new FormData(addFav);
            fetch('/api/cars/' + this.$route.params.id + '/favourite', {
                method: 'POST',
                body: form_data,
                headers: {
                    'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
                    'X-CSRF-TOKEN': this.csrfToken
                }
            })
            .then(function(response) {
                return response.json();
            })
            .then(function(response){
                console.log(response);
                self.message = response.message;
                // router.push('/explore');                
            })
            .catch(function(error) {
                console.log(error);
                self.errorFlask = error.response.data.errors;
            })
        },
         getCsrfToken() {
            let self = this;
            fetch("/api/csrf-token")
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    self.csrfToken = data.csrf_token;
                })
        },
        getCarDetails() {
            let self = this;
            fetch('/api/cars/' + this.$route.params.id)
            .then(function(response) {
                return response.json();
            })
            .then(function(data){
                // response is a dictionary
                // console.log(data);
                self.make = data.make;
                console.log(self.make);
                self.model = data.model;
                self.year = data.year;
                self.price = data.price;
                self.image = data.image;
                self.id = data.id;
                self.transmission = data.transmission;
                self.color = data.color;
                self.car_type = data.car_type;
                self.description = data.description;
            })
            .catch(function(error) {
                console.log(error);
            })
        },

    }
}
</script>
<style>
</style>