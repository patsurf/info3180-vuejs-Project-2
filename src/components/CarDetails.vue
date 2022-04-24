<template>
    <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
    <li v-for="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
    <div class="column">
        <img id="carDetailsIMG" :src="'/uploads/car_photos/'+ image" alt="car image">
    </div>
    <!-- <div class="Cartext" style="float:left; padding: 20px;"> -->
    <div class="Cartext column" style="padding: 20px">
        <h1>{{make}}</h1> 
        <h5>{{model}}</h5>
        <br>
        <br>
        <p style="color: gray;">{{description}}</p>
        <div class="row">
            <div class="column">
                <p>Color <span style="font-weight: bold;">{{color}}</span></p>
            </div>
            <div class="column">
                <p>Body Type  <span style="font-weight: bold;">{{car_type}}</span></p> 
            </div>
        </div>
        <div class="row">
            <div class="column">
                <p>Price <span style="font-weight: bold;">${{price}} </span></p> 
            </div>
            <div class="column">
                <p>Transmission <span style="font-weight: bold;">{{transmission}}</span></p> 
            </div>
        </div>
        <div class="row">
            <div class="column">
                <button type="submit" class="btn btn-success" style="color: white;">Email Owner</button>
                <form class="form" @submit.prevent="addFavorite" id="addFav" method="POST" enctype="multipart/form-data">
                    <input type="hidden" id="user_id" class="form-control" name="user_id" :value="user_id">
                    <button type="submit" class="btn" style="color: red;"><fa icon="heart"/></button>
                </form>          
           </div>
        </div>
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
    computed: {
        price: function () {
            let dollarUS = Intl.NumberFormat('en-US').format(this.price);
            return dollarUS;
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