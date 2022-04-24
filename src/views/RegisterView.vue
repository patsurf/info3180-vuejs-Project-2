<script>
import RegisterForm from '@/components/RegisterForm.vue'
export default {
	data() {
	  return {
	  
	  };
	},
	components: { RegisterForm  }
};


</script>



<template>
		<div class="container">
			<h1 class="h3 mb-3 font-weight-normal">Register New User</h1>
			<div class="regisForm">
				<RegisterForm></RegisterForm>		
			</div>
		</div>
 

</template>




<style>

.container { 
	margin: 0 auto; 
	width: 850px;
	/* background-color: #ffffff; */
	border-radius: 10px;
	padding: 25px;
    /* width: 800px; */
}

.regisForm{
	background-color: #ffffff;
	padding: 40px;
	border-radius: 20px;
}

body {
    padding-top: 5rem;
    background-color: #ececec;
}


/* style for form fields */
[class*="form-group"]{
	font-weight: bold;
	border-radius: 5px;
	display:inline-block;
	padding: 5px;
	width: 47%;
	
	
  	
}

[class*="form-groupbio"]{
	margin-right: 50px;
	
}


#RegisButton {
	margin-top: 10px;
	background-color: #0fb881;
	color: white;
	padding-top: 10px;
	padding-bottom: 10px;
	padding-left: 30px;
	padding-right: 30px;
	border-radius: 5px;
}

#description textarea{
	width: 300px;
}

</style>