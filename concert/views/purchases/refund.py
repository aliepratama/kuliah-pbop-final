import customtkinter


from concert.controllers.purchases import purchases_ctrl
from concert.helpers.session import Session


class RefundPage(customtkinter.CTkFrame):

    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent, fg_color="transparent")
        self.controller = controller
        label = customtkinter.CTkLabel(self, text="Refund", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = customtkinter.CTkButton(self, text="Konfirmasi",
                           command=self._refund)
        button1.pack()
        button2 = customtkinter.CTkButton(self, text="Kembali",
                           command=lambda: controller.show_frame("PurchasePage", True))
        button2.pack()
        
    def _refund(self):
        purchases_ctrl.refund(Session.USER_DATA['purchase_id'])
        self.controller.show_frame("PurchasePage", True)