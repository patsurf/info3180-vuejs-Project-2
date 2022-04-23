<template>
    <form class="form-signin" @submit.prevent="registerUser" id="registerForm" method="POST" enctype="multipart/form-data">
        <div v-if="message" class="alert alert-success" role="alert">{{ message }}</div>
        <li v-for ="err in errorFlask " class="alert alert-danger" role="alert">{{ err }}</li>
        <h1 class="h3 mb-3 font-weight-normal">Register New User</h1>
        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" class="form-control" placeholder="Username" required>
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
        </div>
        <div class="form-group">
            <label for="name">Fullname</label>
            <input type="text" id="name" name="name" class="form-control" placeholder="Name" required>
        </div>
        <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required>
        </div>
        <div class="form-group">
            <label for="location">Location</label>
            <input type="text" id="location" name="location" class="form-control" placeholder="Location" required>
        </div>
        <div class="form-group">
            <label for="biography">Biography</label>
            <textarea id="biography" name="biography" class="form-control" placeholder="Biography" required></textarea>
        </div>
        <div class="form-group">
            <br><label for="photo">Profile Picture</label><br>
           <input type="file" id="photo" class="form-control-file" name="photo" placeholder="Profile Picture" @change="fileSelected" required>
        </div>
        <br><button class="btn btn-lg btn-primary btn-block  bg-dark" type="submit">Register</button> 
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
        registerUser() {
            let registerForm = document.getElementById('registerForm');
            let form_data = new FormData(registerForm);
            let self = this;

            fetch("/api/register", {
                method: 'POST',
                body: form_data,
                headers: { 
                    'X-CSRF-TOKEN': this.csrfToken
                }
            })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    // display a success message if the user is created
                    if (data.message) {
                        console.log(data);
                        self.message = data.message;
                        router.push('/login');
                    } else {
                        self.errorFlask = data.errors;
                    }
                })
                .catch(function (error) {
                    // display an error message
                    self.errorFlask = error.errors;
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