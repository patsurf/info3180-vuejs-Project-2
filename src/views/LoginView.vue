<script>
import LoginForm from '@/components/LoginForm.vue'
export default {
	data() {
	  return {
	  
	  };
	},
	components: { LoginForm  }
};



</script>



<template>
	<div class="container">
		<h1 class="h3 mb-3 font-weight-normal text-center">Login to your account</h1> <br>
    	 <LoginForm></LoginForm>
	</div>

</template>


<style>

body{
    background-color: #ececec;
    display: flex;
    justify-content: center;
    align-items: center;

}

#login{
	width: 100%;
	background-color: #0fb881;
	color: #fff;
}

.container{
	margin-top: 100px;
	width: 500px;
}

#loginForm { 
	margin: 0 auto; 
	box-shadow: 1px 5px 15px gray;
}

[class*="form-signin"]{
	background-color: #ffffff;
	border-radius: 15px;
	padding: 30px;
}

[class*="form-group"]{
	width: 100%;
	margin-bottom: 30px;
}

#loginForm label{
	font-weight: bold;
	font-size: 16px;
}

[class*="btn btn-lg btn-primary"]{
	background-color: rgb(45, 242, 140);
	border-color: rgb(45, 242, 140);
	width: auto;
}

</style>