<template>
    <form class="form-sigin" @submit.prevent="newCar" id="CarForm" method="POST" enctype="multipart/form-data">
        <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
        <li v-for="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
        <h1 class="h3 mb-3 font-weight-normal">Add New Car</h1>
        <div class="form-row ">
            <div class="form-group col-md-4">
                <label for="make">Make</label>
                <input type="text" class="form-control" id="make" name="make" v-model="make" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="model">Model</label>
                <input type="text" class="form-control" id="model" name="model" v-model="model" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="year">Year</label>
                <input type="text" class="form-control" id="year" name="year" v-model="year" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="color">Color</label>
                <input type="text" class="form-control" id="color" name="color" v-model="color" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="price">Price</label>
                <input type="number" class="form-control" id="price" name="price" v-model="price" placeholder="Numbers only" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="car_type">Car Type</label>
                <select name="car_type" id="car_type" v-model="car_type" required>
                    <option value="Sedan">Sedan</option>
                    <option value="SUV">SUV</option>
                    <option value="Coupe">Coupe</option>
                    <option value="Convertible">Convertible</option>
                    <option value="Crossover">Crossover</option>
                    <option value="Hatchback">Hatchback</option>
                    <option value="Pickup">Pickup</option>
                    <option value="Van">Van</option>
                    <option value="Wagon">Wagon</option>
                    <option value="Sports_Car">Sports Car</option>
                </select>
            </div>
            <div class="form-group col-md-4 ">
                <label for="transmission">Transmission</label>
                <select name="transmission" id="transmission" v-model="transmission" required>
                    <option value="automatic">Automatic</option>
                    <option value="manual">Manual</option>
                </select>
            </div>
            <div class="form-group col-md-10 ">
                <br>
                <label for="description">Description</label>
                <textarea type="description" class="form-control" id="description" v-model="description" name="description"></textarea>
            </div>
            <br>
            <label for="image">Upload Photo</label>
            <br>
            <div class="form-group">
                <input type="file" id="image" class="form-control-file" name="image"
                    @change="fileSelected" required>
                <input type="hidden" id="user_id" class="form-control" name="user_id" :value="user_id">
            
            </div>
            <br>
            <button type="submit" class="btn btn-primary" @click.prevent="newCar">Register</button>
            <!-- <button type="reset" name="reset" class="btn btn-warning">Undo all</button> -->

        </div>
    </form>
</template>

<script>
import router from "../router";
import store from '@/main.js'; 

export default {
    data() {
        return {
            csrfToken: '',
            user_id: '',
            errorFlask: [],
            message: '',
            make: '',
            model: '',
            year: '',
            color: '',
            price: '',
            car_type: '',
            transmission: '',
            description: ''
        }
    },
    computed: {
        user_id: function () {
            return parseInt(sessionStorage.getItem('user_id'));
        }
    },

    created() {
        this.getCsrfToken();
    },
    methods: {
        newCar(){
            let self = this;
            let CarForm = document.getElementById('CarForm');
            let form_data = new FormData(CarForm);
            fetch('/api/cars', {
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
            .then(function(data){
                console.log(data);
                self.message = data.message;
                if(data.errors.length > 0) {
                    self.errorFlask = data.errors;
                }
                router.push('/explore');                
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
        }
    }
}
         
</script>



