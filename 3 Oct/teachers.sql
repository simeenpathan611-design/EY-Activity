use university
switched to db university
db["teachers"].find()
db.teachers.insertMany([
  {teacher_id:1,name:"Priya",age:22,city:"Delhi",course:"ML"},
  {teacher_id:2,name:"Arjun",age:20,city:"Bengaluru",course:"Data Science"},
  {teacher_id:3,name:"Neha",age:23,city:"Hyderabad",course:"AI"},
  {teacher_id:4,name:"Vikram",age:21,city:"Chennai",course:"ML"}
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfb39984eb0480e7682cd4'),
    '1': ObjectId('68dfb39984eb0480e7682cd5'),
    '2': ObjectId('68dfb39984eb0480e7682cd6'),
    '3': ObjectId('68dfb39984eb0480e7682cd7')
  }
}
db.teachers.find()
{
  _id: ObjectId('68dfb39984eb0480e7682cd4'),
  teacher_id: 1,
  name: 'Priya',
  age: 22,
  city: 'Delhi',
  course: 'ML'
}
{
  _id: ObjectId('68dfb39984eb0480e7682cd5'),
  teacher_id: 2,
  name: 'Arjun',
  age: 20,
  city: 'Bengaluru',
  course: 'Data Science'
}
{
  _id: ObjectId('68dfb39984eb0480e7682cd6'),
  teacher_id: 3,
  name: 'Neha',
  age: 23,
  city: 'Hyderabad',
  course: 'AI'
}
{
  _id: ObjectId('68dfb39984eb0480e7682cd7'),
  teacher_id: 4,
  name: 'Vikram',
  age: 21,
  city: 'Chennai',
  course: 'ML'
}
db.teachers.findOne({name:"Rahul"})
null
db.teachers.findOne({name:"Arjun"})
{
  _id: ObjectId('68dfb39984eb0480e7682cd5'),
  teacher_id: 2,
  name: 'Arjun',
  age: 20,
  city: 'Bengaluru',
  course: 'Data Science'
}
db.teachers.find({course:"AI")
SyntaxError: Unexpected token, expected "," (1:29)

[0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mteachers[33m.[39mfind({course[33m:[39m[32m"AI"[39m)
 [90m   |[39m                              [31m[1m^[22m[39m[0m
db.teachers.find({course:"AI"})
{
  _id: ObjectId('68dfb39984eb0480e7682cd6'),
  teacher_id: 3,
  name: 'Neha',
  age: 23,
  city: 'Hyderabad',
  course: 'AI'
}
db.teachers.find({},{name:1,course:1,_id:0})
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
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 0,
  upsertedCount: 0
}

db.teachers.updateMany(
  {course:"AI"},
  {$set:{grade:"A"}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
db.teachers.deleteOne({name:"Arjun"})
{
  acknowledged: true,
  deletedCount: 1
}
university
Selection deleted

