import os
file_output = "file.sqlite"
from simple_graph_sqlite import database as db
db.initialize(file_output)

# Have commented the insertion code as already inserted in db
'''db.atomic(file_output,db.add_node({'name':'A'},1))
db.atomic(file_output,db.add_node({'name':'B'},2))
db.atomic(file_output,db.add_node({'name':'C'},3))
db.atomic(file_output,db.add_node({'name':'D'},4))
db.atomic(file_output,db.add_node({'name':'E'},5))
db.atomic(file_output,db.add_node({'name':'F'},6))
db.atomic(file_output,db.add_node({'name':'G'},7))
db.atomic(file_output,db.add_node({'name':'H'},8))
db.atomic(file_output,db.add_node({'name':'I'},9))
db.atomic(file_output, db.connect_nodes(1,2))
db.atomic(file_output, db.connect_nodes(1,3))
db.atomic(file_output, db.connect_nodes(1,5))
db.atomic(file_output, db.connect_nodes(1,7))
db.atomic(file_output, db.connect_nodes(1,9))
db.atomic(file_output, db.connect_nodes(2,1))
db.atomic(file_output, db.connect_nodes(2,2))
db.atomic(file_output, db.connect_nodes(2,5))
db.atomic(file_output, db.connect_nodes(2,6))
db.atomic(file_output, db.connect_nodes(2,8))
db.atomic(file_output, db.connect_nodes(3,1))
db.atomic(file_output, db.connect_nodes(3,5))
db.atomic(file_output, db.connect_nodes(3,6))
db.atomic(file_output, db.connect_nodes(3,7))
db.atomic(file_output, db.connect_nodes(3,9))
db.atomic(file_output, db.connect_nodes(4,1))
db.atomic(file_output, db.connect_nodes(4,2))
db.atomic(file_output, db.connect_nodes(4,3))
db.atomic(file_output, db.connect_nodes(4,5))
db.atomic(file_output, db.connect_nodes(4,7))
db.atomic(file_output, db.connect_nodes(4,8))
db.atomic(file_output, db.connect_nodes(5,2))
db.atomic(file_output, db.connect_nodes(5,5))
db.atomic(file_output, db.connect_nodes(5,6))
db.atomic(file_output, db.connect_nodes(5,8))
db.atomic(file_output, db.connect_nodes(6,1))
db.atomic(file_output, db.connect_nodes(6,6))
db.atomic(file_output, db.connect_nodes(6,7))
db.atomic(file_output, db.connect_nodes(6,8))
db.atomic(file_output, db.connect_nodes(7,4))
db.atomic(file_output, db.connect_nodes(7,7))
db.atomic(file_output, db.connect_nodes(8,1))
db.atomic(file_output, db.connect_nodes(8,3))
db.atomic(file_output, db.connect_nodes(8,4))
db.atomic(file_output, db.connect_nodes(8,5))
db.atomic(file_output, db.connect_nodes(8,6))
db.atomic(file_output, db.connect_nodes(8,9))
db.atomic(file_output, db.connect_nodes(9,1))
db.atomic(file_output, db.connect_nodes(9,2))
db.atomic(file_output, db.connect_nodes(9,3))
db.atomic(file_output, db.connect_nodes(9,4))
db.atomic(file_output, db.connect_nodes(9,9))
db.visualize(file_output, 'new1.dot',[1,2,3,4,5,6,7,8,9])'''
dict1 = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I"}
dictrev = {v:k for k,v in dict1.items()}
def one_hop(element):
    ''' returns all possible outward movements by one hop '''
    listresult = []
    for i in db.atomic(file_output,db.get_connections_one_way(dictrev[element], direction=db.connections_in)):
        listresult.append(dict1[int(i[1])])
    #print(listresult)
    return listresult
def twohops(element):
    ''' returns all possible outwards hops by two hops '''
    res_one_hop = one_hop(element)
    listnew = []
    for ii in res_one_hop:
        for jj in db.atomic(file_output, db.get_connections_one_way(dictrev[ii], direction=db.connections_in)):
            listnew.append("I->"+ii+"->"+dict1[int(jj[1])]) 
    return listnew

list_for_1_hop = ["A","D","E"]
list_for_2_hop = ["I"]

for element in list_for_1_hop:
    print(element,one_hop(element))
#Output 
#A ['B', 'C', 'E', 'G', 'I']
#D ['A', 'B', 'C', 'E', 'G', 'H']
#E ['B', 'E', 'F', 'H']
for ele in list_for_2_hop:
    print(ele,twohops(ele))
# Output
#I ['I->A->B', 'I->A->C', 'I->A->E', 'I->A->G', 'I->A->I', 'I->B->A', 'I->B->B', 'I->B->E', 'I->B->F', 'I->B->H', 'I->C->A', 'I->C->E', 'I->C->F', 'I->C->G', 'I->C->I', 'I->D->A', 'I->D->B', 'I->D->C', 'I->D->E', 'I->D->G', 'I->D->H', 'I->I->A', 'I->I->B', 'I->I->C', 'I->I->D', 'I->I->I']    

 