db.students.insertOne({
  student_id:1,
  name:"Rahul",
  age:21,
  city:"Mumbai",
  course:"AI",
  marks:85
})
{
  acknowledged: true,
  insertedId: ObjectId('68dfa5468f010c579ae01ee8')
}
db.students.insertMany([
  {student_id:2,name:"Priya",age:22,city:"Delhi",course:"ML",marks:90},
  {student_id:3,name:"Arjun",age:20,city:"Bengaluru",course:"Data Science",marks:78},
  {student_id:4,name:"Neha",age:23,city:"Hyderabad",course:"AI",marks:88},
  {student_id:5,name:"Vikram",age:21,city:"Chennai",course:"ML",marks:95}
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfa6bc8f010c579ae01ee9'),
    '1': ObjectId('68dfa6bc8f010c579ae01eea'),
    '2': ObjectId('68dfa6bc8f010c579ae01eeb'),
    '3': ObjectId('68dfa6bc8f010c579ae01eec')
  }
}
db.students.find()
{
  _id: ObjectId('68dfa411c07db3773e6fd9d0')
}
{
  _id: ObjectId('68dfa5468f010c579ae01ee8'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
{
  _id: ObjectId('68dfa6bc8f010c579ae01ee9'),
  student_id: 2,
  name: 'Priya',
  age: 22,
  city: 'Delhi',
  course: 'ML',
  marks: 90
}
{
  _id: ObjectId('68dfa6bc8f010c579ae01eea'),
  student_id: 3,
  name: 'Arjun',
  age: 20,
  city: 'Bengaluru',
  course: 'Data Science',
  marks: 78
}
{
  _id: ObjectId('68dfa6bc8f010c579ae01eeb'),
  student_id: 4,
  name: 'Neha',
  age: 23,
  city: 'Hyderabad',
  course: 'AI',
  marks: 88
}
{
  _id: ObjectId('68dfa6bc8f010c579ae01eec'),
  student_id: 5,
  name: 'Vikram',
  age: 21,
  city: 'Chennai',
  course: 'ML',
  marks: 95
}
db.students.findOne({name:"Rahul"})
{
  _id: ObjectId('68dfa5468f010c579ae01ee8'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
db.students.find({marks{$gt:85}})
SyntaxError: Unexpected token, expected "," (1:23)

[0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mstudents[33m.[39mfind({marks{$gt[33m:[39m[35m85[39m}})
 [90m   |[39m                        [31m[1m^[22m[39m[0m
db.students.find({marks:{$gt:85}})
{
  _id: ObjectId('68dfa6bc8f010c579ae01ee9'),
  student_id: 2,
  name: 'Priya',
  age: 22,
  city: 'Delhi',
  course: 'ML',
  marks: 90
}
{
  _id: ObjectId('68dfa6bc8f010c579ae01eeb'),
  student_id: 4,
  name: 'Neha',
  age: 23,
  city: 'Hyderabad',
  course: 'AI',
  marks: 88
}
{
  _id: ObjectId('68dfa6bc8f010c579ae01eec'),
  student_id: 5,
  name: 'Vikram',
  age: 21,
  city: 'Chennai',
  course: 'ML',
  marks: 95
}
db.students.find({},{name,:1,course:1,_id:0})
SyntaxError: Unexpected token (1:26)

[0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mstudents[33m.[39mfind({}[33m,[39m{name[33m,[39m[33m:[39m[35m1[39m[33m,[39mcourse[33m:[39m[35m1[39m[33m,[39m_id[33m:[39m[35m0[39m})
 [90m   |[39m                           [31m[1m^[22m[39m[0m
db.students.find({},{name:1,course:1,_id:0})
{}
{
  name: 'Rahul',
  course: 'AI'
}
{
  name: 'Priya',
  course: 'ML'
}
{
  name: 'Arjun',
  course: 'Data Science'
}
{
  name: 'Neha',
  course: 'AI'
}
{
  name: 'Vikram',
  course: 'ML'
}
db.students.updateOne(
  {name:"Neha"},
  {$set:{marks:92,course:"Advanced AI"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.students.updateMany(
  {course:"AI"},
  {$set:{grade:"A"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.students.deleteOne({name:"Arjun"})
{
  acknowledged: true,
  deletedCount: 1
}
db.students.deleteMany({marks:{$lt:80}})
