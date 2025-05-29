class dept:
  dc=0
  def __init__(self,id,dname,loc,hod):
    self.id=id
    self.dname=dname
    self.loc=loc
    self.hod=hod
    dept.dc+=1
  def display_info(self):
    print(f"Department id: {self.id}")
    print(f'Department name: {self.dname}')
    print(f'location: {self.loc}')
    print(f"hod: {self.hod}")
    print(f'Department count: {self.dc}')
dept1=dept(1,"eee","hyd","asriya\n")
dept1.display_info()
dept2=dept(2,"ece","hyd","manasa\n")
dept2.display_info()

class dept:

  def __init__(self, id, dname, loc, hod):
    self.id = id
    self.dname = dname
    self.loc = loc
    self.hod = hod

  def display_info(self):
    print(f"\nDepartment id: {self.id}")
    print(f"Department name: {self.dname}")
    print(f"Location: {self.loc}")
    print(f"HOD: {self.hod}")

dept2 = int(input("Enter number of departments: "))
l = []

for i in range(dept2):
  print(f"\nEnter details for department {i+1}")
  id = int(input("Enter department id: "))
  dname = input("Enter department name: ")
  location = input("Enter location: ")
  hod = input("Enter name of HOD: ")
  dept1 = dept(id, dname, location, hod)
  l.append(dept1)

print("\n--- Department Details ---")
for department in l:
  department.display_info()


search_id = int(input("\nEnter department id to search: "))

found = False
for department in l:
    if department.id == search_id:
        print("\n--- Department Found ---")
        department.display_info()
        found = True
        break

if not found:
    print("Department not found.")