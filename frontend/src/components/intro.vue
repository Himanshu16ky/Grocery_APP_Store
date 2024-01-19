<template>
        <div
      class="c1"
      style="background-color: #096767; height: 100vh; width: 100vw"
    >
      <div
        class="c2"
        style="width: 60%; height: 80%; position: relative; top: 10%; left: 20%"
      >
        <img
          style="
            border-radius: 40px;
            width: 100%;
            height: 100%;
            box-shadow: rgba(0, 0, 0, 0.401) 20px 20px 30px 20px;
          "
          src="../assets/bg_image_1copy.jpeg"
          alt="aedgv"
        />
        <div
          class="c3"
          style="position: absolute; top: 25%; left: 30%; text-align: center"
        >
          <div>
            <h1
              style="
                color: #e3a906;
                font-family: 'Droid serif', serif;
                font-size: 55px;
                font-weight: 500;
                font-style: italic;
                line-height: 44px;
                margin: 0 0 12px;
                text-align: center;
              "
            >
              Snapshop
            </h1>
            <br />
            <br />
            <p
              style="
              color: #78bebe;
                font-family: 'Oleo Script', cursive;
                font-size: 20px;
                font-weight: normal;
                line-height: 32px;
                margin: 0 0 18px;
                text-shadow: 1px 0 0 #fff;
              "
            >
              Fresh Deals Await! Sign in to Your Grocery <br />
              Wonderland and Let the Shopping Begin!
            </p>
            <!-- HTML !-->
            <button
            @click="tologin()"
              class="button-29"
              style="font-family: 'Oleo Script', cursive"
              role="button"
            >
              Login
            </button>
            <button
            @click="tosignup()"
              class="button-29"
              style="
                font-family: 'Oleo Script', cursive;
                background-image: radial-gradient(
                  100% 100% at 100% 0,
                  #fff200 0,
                  #ffb803 100%
                );
              "
              role="button"
            >
              SignUp
            </button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Intro',
  props: {
    total_items:Number,
    total_price:Number,
    // cart_items:[],
  },
  mounted(){
    
  },
  methods: {
    tologin() {
      this.$router.push(`/login`);
    },
    tosignup() {
      this.$router.push(`/register`);
    },
  },
  }
</script>


<style scoped>
.button-29 {
  align-items: center;
  appearance: none;
  background-image: radial-gradient(
    100% 100% at 100% 0,
    #5adaff 0,
    #5468ff 100%
  );
  border: 0;
  border-radius: 6px;
  box-shadow: rgba(45, 35, 66, 0.4) 0 2px 4px,
    rgba(45, 35, 66, 0.3) 0 7px 13px -3px, rgba(58, 65, 111, 0.5) 0 -3px 0 inset;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  font-family: "JetBrains Mono", monospace;
  height: 48px;
  justify-content: center;
  line-height: 1;
  list-style: none;
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  position: relative;
  text-align: left;
  text-decoration: none;
  transition: box-shadow 0.15s, transform 0.15s;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  will-change: box-shadow, transform;
  font-size: 18px;
  margin: 15px;
}

.button-29:focus {
  box-shadow: #000000 0 0 0 1.5px inset, rgba(45, 35, 66, 0.4) 0 2px 4px,
    rgba(45, 35, 66, 0.3) 0 7px 13px -3px,
    rgba(60, 224, 128, 0.886) 0 -3px 0 inset;
}

.button-29:hover {
  box-shadow: rgba(45, 35, 66, 0.4) 0 4px 8px,
    rgba(45, 35, 66, 0.3) 0 7px 13px -3px, #000000 0 -3px 0 inset;
  transform: translateY(-2px);
}

.button-29:active {
  box-shadow: #000000 0 3px 7px inset;
  transform: translateY(2px);
}
</style>