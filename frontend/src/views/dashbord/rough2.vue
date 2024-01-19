
<template>
  <div>
    <div data-v-26fcafcc="" class="card">
      <div data-v-26fcafcc="" class="card-header p-3">
        <h5 data-v-26fcafcc="" class="mb-0">
          <i data-v-26fcafcc="" class="fas fa-tasks me-2"></i> Adding Categories
        </h5>
      </div>
      <div
        data-v-26fcafcc=""
        class="card-body"
        data-mdb-perfect-scrollbar="true"
      >
        <table data-v-26fcafcc="" class="table mb-0">
          <thead data-v-26fcafcc="">
            <tr data-v-26fcafcc="">
              <th data-v-26fcafcc="" scope="col">Serial n.o</th>
              <th data-v-26fcafcc="" scope="col">Name</th>
              <th data-v-26fcafcc="" scope="col">Category</th>
              <th data-v-26fcafcc="" scope="col">Actions</th>
            </tr>
          </thead>
          <tbody data-v-26fcafcc=""></tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      shopData: {
        category1: [
          { product_name: "item1", quantity: 0 },
          { product_name: "item2", quantity: 0 },
        ],
        category2: [
          { product_name: "item3", quantity: 0 },
          { product_name: "item4", quantity: 0 },
        ],
      },
      userData: [
        { product_name: "item2", item_count: 3 },
        { product_name: "item4", item_count: 2 },
      ],
    };
  },
  methods: {
    updateShopDataWithUserData() {
      for (const category in this.shopData) {
        for (const product of this.shopData[category]) {
          const matchingUserData = this.userData.find(
            (userProduct) => userProduct.product_name === product.product_name
          );

          if (matchingUserData) {
            // Update the quantity in shopData based on userData
            product.quantity = matchingUserData.item_count;
          }
        }
      }
    },
  },
  mounted() {
    // Call the updateShopDataWithUserData method when the component is mounted
    this.updateShopDataWithUserData();
  },
};
</script>
