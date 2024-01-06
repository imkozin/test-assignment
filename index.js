const item = {
  name: 'some_name',
  body: 'some_description',
  describe: function () {
    // describe: () => {
    console.log(`Item [${this.name}] contains: ${this.body}`)
  },
}
item.describe()

// const userData = JSON.parse(userInput)
// const query = `SELECT * FROM users WHERE name = '${userData.name}' AND password = '${userData.password}'`

const userData = JSON.parse(userInput)
const query = 'SELECT * FROM users WHERE name = ? AND password = ?'
// Пример использования библиотеки для параметризации запроса
db.query(query, [userData.name, userData.password], (error, results) => {
  // Обработка результатов запроса
})
