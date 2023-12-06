
// get state names

states = document.getElementById("col1").getElementsByClassName("Data l")

state_names = []

for (const state of states) { state_names.push(state.getElementsByTagName("a")[0].innerHTML) }

console.log(state_names)

// get bar values

bars = document.getElementById("barchart").getElementsByClassName("bar")

data_values = []

for (const bar of bars) { data_values.push(bar.__data__.number) }

console.log(document.getElementById("title_label").textContent + "\n" + data_values.join(','))

// data organization
// date1 state city reason number
// date2 state city reason number

// date state/city reason citizenship value

// https://trac.syr.edu/phptools/immigration/remove/table.php?stat=count&citizenship=2&fymon=103&depart_city=21&most_ser_crim_conv_mscc2=1&dimension=most_ser_crim_conv_mscc2&sort=valdesc
// https://trac.syr.edu/phptools/immigration/remove/table.php?stat=count&citizenship=2&fymon=103&depart_city=21&most_ser_crim_conv_mscc2=1&dimension=most_ser_crim_conv_mscc&dimension=citizenship&sort=valdesc
