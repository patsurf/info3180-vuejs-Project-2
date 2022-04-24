<template>
    <div class="container carDetails row">
        <CarDetails></CarDetails>
    </div>
</template>
<script>
    import CarDetails from "../components/CarDetails.vue";
    export default {
        data() {
            return {};
        },
        components: {
            CarDetails
        }
    }


</script>
<style>
    .carDetails {
        background-color: #ffffff;
        border-radius: 20px;
        height: auto;
        overflow: hidden;
        width: auto;
        margin: 0 auto;
        padding: 20px;
    }
    body { background-color: #ececec; }
    #carDetailsIMG{
        /* right: 50%; */
        position: relative;
        /* transform: translate(-50%, 0); */
        width: 600px;
        /* margin-top:0px; */
    }
    /* span{
        padding-left: 15px;
        padding-right: 15px;

    } */
    .column {
        flex: 50%;
        padding: 10px;
    }
    .row {
        display:flex;
    }
</style>