
#------crate a tabel------



from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("type", ["Electirc", "Water", "Fire"])
table.align = "r"
print(table)
