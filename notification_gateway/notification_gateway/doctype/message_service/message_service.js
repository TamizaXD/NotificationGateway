// Copyright (c) 2024, mohammed and contributors
// For license information, please see license.txt

frappe.ui.form.on("Message Service", {
	refresh(frm) {

        // frm.add_custom_button(("Send Message"), function(){
        //     cusotmer_name = frm.doc.name;

        //     frappe.call({
        //         // method: "rentals.apis.api.send_message?name="+cusotmer_name, //this button triggers the API and take one parameter 'name' to uniquely identify each record in the Message Service Doctype 
        //         // method: "rentals.methods.test_schedulers.send_html_email",
        //     })
        //     console.log("Message sent!")
        // })
	},
    onload: function(frm){
        toggle_section(frm);       
    },

    service_type: function(frm){
        toggle_section(frm);
        frm.save();
    }
});

function toggle_section (frm){
    // 0 to show and 1 to hide
    sms = 0
    whatsapp = 0
    
    if(frm.doc.service_type === 'Both'){
        sms = 0
        whatsapp = 0
    }

    else if (frm.doc.service_type === 'SMS') { 
        sms = 0
        whatsapp = 1
        
    } else {
        sms = 1
        whatsapp = 0
    }

    frm.fields_dict['service_type_sms_section'].df.hidden = sms;
    frm.fields_dict['service_type_whatsapp_section'].df.hidden = whatsapp; 
}
