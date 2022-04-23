<template>
    <h3>Explore Cars</h3>
    <form class="form" @submit.prevent="carSearch" id="CarSearchForm" method="POST" enctype="multipart/form-data">
        <!-- <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div> -->
        <li v-for="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
        <div class="form-group col-md-4">
            <label for="make">Make</label>
            <input type="text" class="form-control" id="make" name="make" v-model="make">
        </div>
        <div class="form-group col-md-4 ">
            <label for="model">Model</label>
            <input type="text" class="form-control" id="model" name="model" v-model="model">
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Search</button>
    </form>
    <br>
    <br>
    <!-- If no search is done show cards -->
    <div v-if="!carSearch">
        <div class="card-deck">
            <div v-for="car in cars" class="card">
                <img class="card-img-top" :src="'/uploads/car_photos/' + car.image" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ car.make }} {{ car.model }}</h5>
                    <p class="card-text">{{ car.year }}</p>
                    <p class="card-text">{{ car.price }}</p>
                    <a :href="'/cars/' + car.id" class="btn btn-primary">View more details</a>
                </div>
            </div>
        </div>
    </div>
    <!-- If search is done show search results -->
    <div v-else>
        <div class="card-deck">
            <div v-for="car in cars" class="card">
                <img class="card-img-top" :src="'/uploads/car_photos/' + car.image" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ car.make }} {{ car.model }}</h5>
                    <p class="card-text">{{ car.year }}</p>
                    <p class="card-text">{{ car.price }}</p>
                    <a :href="'/cars/' + car.id" class="btn btn-primary">View more details</a>
                </div>
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
            // user_id: '',
            errorFlask: [],
            message: '',
            make: '',
            model: '',
            year: '',
            price: '',
            image: '',
            id: '',
            cars: []
        }
    },

    created() {
        this.getCsrfToken();
        this.getCarList();
    },

    methods: {
        carSearch() {
            let self = this;
            let CarSearchForm = document.getElementById('CarSearchForm');
            let form_data = new FormData(CarSearchForm);
            fetch('/api/search', {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRF-TOKEN': this.csrfToken,
                    'Authorization': 'Bearer ' + sessionStorage.getItem('token')
                }
            }).then(function (response) {
                return response.json();
            }).then(function (data) {
                self.cars = data.allCars;
                console.log(data.allCars);
                self.message = data.message;
                console.log(self.message);
                if(data.errors.length > 0) {
                    self.errorFlask = data.errors;
                }
            }).catch(function (error) {
                self.errorFlask = error.errors;
                console.log(error);
            });
        },

        getCarList() {
            let self = this;
            fetch('/api/cars', {
                method: 'GET',
                headers: {
                    'X-CSRF-TOKEN': this.csrfToken,
                    'Authorization': 'Bearer ' + sessionStorage.getItem('token')
                }
            }).then(function (response) {
                return response.json();
            }).then(function (data) {
                // the data is an array of cars
                self.message = data.message;
                console.log(self.message);
                self.cars = data.allCars;
                console.log(data.allCars);
            }).catch(function (error) {
                console.log(error);
            });
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
        }
    }
}
</script>
<style>
</style>