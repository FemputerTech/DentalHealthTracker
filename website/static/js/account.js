class Account {
  constructor(user) {
    this.user = user;
    this.init();
  }

  init() {
    this.displayUser();
  }

  displayUser() {
    const accountNumber = document.querySelector(".user-account");
    const name = document.querySelector(".user-name");
    const email = document.querySelector(".user-email");
    const dob = document.querySelector(".user-dob");
    const tel = document.querySelector(".user-tel");
    const dentist = document.querySelector(".user-dentist");

    accountNumber.textContent = `Account: ${this.user.account_number}`;
    name.textContent = `${this.user.first_name} ${this.user.last_name}`;
    email.textContent = this.user.email;
    dob.textContent = this.user.dob;
    tel.textContent = this.user.tel;
    dentist.textContent = this.user.dentist;
  }
}
