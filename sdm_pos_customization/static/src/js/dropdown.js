import { Navbar } from "@point_of_sale/app/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(Navbar.prototype, {
            custom(){
                prompt("Help!Enter your problem")
            }

})
