import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";



patch(ControlButtons.prototype, {
   onClickExtraButton() {
        prompt("Thank you for your interaction!");
    },

})
