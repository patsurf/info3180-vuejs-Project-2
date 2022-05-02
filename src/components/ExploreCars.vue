<template>
    <h1>Explore</h1>
    <br>

    <div class="alert alert alert-warning alert-dismissible alert-success" role="alert">If the list of cars appear to be jumbled kindly refresh your page. Thank You</div>'
    <form class="form" @submit.prevent="carSearch" id="CarSearchForm" method="POST" enctype="multipart/form-data">
        <!-- <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div> -->
        <li v-for="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
        <div class="CSF form-group col-md-4">
            <label for="make">Make</label>
            <input type="text" class="form-control" id="make" name="make" v-model="make">
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
        <div class="card-deck ">
            <div v-for="car in cars" class="card">
                <img class="card-img-top" id="car_images" :src="'/uploads/' + car.image" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ car.year }} {{ car.make }}<button class="tags"><fa icon="tags"/> ${{ car.price }}</button></h5>
                    <p class="card-text">{{ car.model }}</p>
                    <button class=" View btn btn-primary"> <a id="id" :href="'/cars/' + car.id">View more details</a></button>
                </div>
            </div>
        </div>
    </div>
    <!-- If search is done show search results -->
    <div v-else>
        <div class="card-deck">
            <div v-for="car in cars" class="card">
                <img class="card-img-top" id="car_images" :src="'/uploads/' + car.image" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">{{ car.year }} {{ car.make }}<button class="tags"><fa icon="tags"/> ${{ car.price }}</button></h5>
                    <p class="card-text">{{ car.model }}</p>
                    <button class="View btn btn-primary"> <a id="id" :href="'/cars/' + car.id" >View more details</a></button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import router from "../router";
import store from '@/main.js';

// refresh page on load
// window.onload = function() {
//     location.reload();
// }

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
    computed: {
    price: function () {
        let dollarUS = Intl.NumberFormat('en-US').format(this.price);
        return dollarUS;
        },
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