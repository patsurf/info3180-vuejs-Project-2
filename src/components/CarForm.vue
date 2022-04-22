<template>
    <form class="form-sigin" @submit.prevent="newCar" id="newCarForm" method="POST" enctype="multipart/form-data">
        <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
        <li v-for="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
        <h1 class="h3 mb-3 font-weight-normal">Add New Car</h1>
        <div class="form-row ">
            <div class="form-group col-md-4">
                <label for="make">Make</label>
                <input type="text" class="form-control" id="make" name="make" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="model">Model</label>
                <input type="text" class="form-control" id="model" name="model" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="colour">Colour</label>
                <input type="text" class="form-control" id="colour" name="colour" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="price">Price</label>
                <input type="text" class="form-control" id="price" name="price" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="car_type">Car Type</label>
                <input type="text" class="form-control" id="car_type" name="car_type" required>
            </div>
            <div class="form-group col-md-4 ">
                <label for="transmission">Transmission</label>
                <input type="text" class="form-control" id="transmission" name="transmission" required>
            </div>
            <div class="form-group col-md-10 ">
                <label for="discription">Description</label>
                <textarea type="description" class="form-control" id="discription" name="discription"></textarea>
            </div>
        </div>
        <br>
        <label for="photo">Upload Photo</label>
        <br>
        <div class="form-group">
            <input type="file" id="photo" class="form-control-file" name="photo"
                @change="fileSelected" required>
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</template>

<script>
import router from "../router";

export default {
    data() {
        return {
            csrfToken: '',
            errorFlask: [],
            message: ''
        }
    },

    created() {
        this.getCsrfToken();
    },
    methods: {
        newCar(){
            let self = this;
            fetch('/api/secure',{
                'headers': {
                    'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
                }
            })
            .then(function(response) {
                return response.json();
            })
            .then(function(response) {
                let result = response.data;
                console.log(result);
                self.user_id = result.user_id;
                return result.user_id
            })
            .then(function(user_id) {
                let self = this;
                let newCarForm = document.getElementById('newCarForm');
                let form_data = new FormData(newCarForm);
                fetch('/api/cars/' + user_id, {
                    method: 'POST',
                    body: form_data,
                    headers: {
                        'Authorization': 'Bearer ' + sessionStorage.getItem('token'),
                        'X-CSRF-TOKEN': self.csrfToken
                    }
                })
                .then(function(response) {
                    return response.json();
                })
                .then(function(response){
                    console.log(response);
                    router.push('/');
                    self.message = response;
                })
                .catch(function(error) {
                    console.log(error);
                    self.errorFlask = error.response.data.errors;
                })
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



