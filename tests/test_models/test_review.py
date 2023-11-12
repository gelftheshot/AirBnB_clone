#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models import storage
FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.user_id = ""
        self.review.place_id = ""
        self.review.text = ""

    def test_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_inheritance(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_id_is_string(self):
        self.assertIsInstance(self.review.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.review.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.review.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.review.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.review.created_at, datetime)
    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)

    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)

    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)
    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_attributes(self):
        self.assertTrue("place_id" in self.review.__dict__)
        self.assertTrue("user_id" in self.review.__dict__)
        self.assertTrue("text" in self.review.__dict__)

class TestReviewInheritedInit(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review1 = Review()
        self.review2 = Review()

    def test_init(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.review.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.review.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.review.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.review.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.review.created_at, datetime)

    def test_review_instantiates_with_kwargs(self):
        review = Review(text="Test", rating=5)
        self.assertEqual(review.text, "Test")
        self.assertEqual(review.rating, 5)


    def test_two_reviews_different_created_at(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_two_reviews_different_updated_at(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.review.updated_at, datetime)


    def test_id_is_unique(self):
        self.assertNotEqual(self.review1.id, self.review2.id)

    def test_review_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_review_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_instantiates_without_args(self):
        self.assertEqual(Review, type(Review()))

    def test_new_review_instance_in_objects(self):
        self.assertIn(Review(), storage.all().values())

    def test_review_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

class TestReviewStr(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_str(self):
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_str_format(self):
        expected_str_format = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str_format)

class TestReviewSave(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_save(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        old_created_at = self.review.created_at
        self.review.save()
        self.assertEqual(self.review.created_at, old_created_at)

    def test_save_changes_updated_at(self):
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)

    def test_save_updates_updated_at(self):
        updated_at_before_save = self.review.updated_at
        self.review.save()
        updated_at_after_save = self.review.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(12)
class TestReviewToDict(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.new_attr = "new attribute value"
        self.review.int_attr = 66

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["created_at"], self.review.created_at.strftime(FORMAT))
        self.assertEqual(review_dict["updated_at"], self.review.updated_at.strftime(FORMAT))

    def test_to_dict_returns_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        review_dict = self.review.to_dict()
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)

    def test_to_dict_formats_dates(self):
        review_dict = self.review.to_dict()
        created_at = datetime.strptime(review_dict["created_at"], FORMAT)
        updated_at = datetime.strptime(review_dict["updated_at"], FORMAT)
        self.assertEqual(created_at, self.review.created_at)
        self.assertEqual(updated_at, self.review.updated_at)

    def test_to_dict_includes_all_attributes(self):
        review_dict = self.review.to_dict()
        self.assertIn("new_attr", review_dict)
        self.assertEqual(review_dict["new_attr"], "new attribute value")

    def test_to_dict_handles_non_string_attributes(self):
        review_dict = self.review.to_dict()
        self.assertIn("int_attr", review_dict)
        self.assertEqual(review_dict["int_attr"], 66)


    def test_to_dict_handles_boolean_attributes(self):
        self.review.bool_attr = True
        review_dict = self.review.to_dict()
        self.assertIn("bool_attr", review_dict)
        self.assertEqual(review_dict["bool_attr"], True)

    def test_to_dict_handles_list_attributes(self):
        self.review.list_attr = [1, 2, 3]
        review_dict = self.review.to_dict()
        self.assertIn("list_attr", review_dict)
        self.assertEqual(review_dict["list_attr"], [1, 2, 3])

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.review.to_dict(12)

    def test_to_dict_handles_tuple_attributes(self):
        self.review.tuple_attr = (4, 5, 6)
        review_dict = self.review.to_dict()
        self.assertIn("tuple_attr", review_dict)
        self.assertEqual(review_dict["tuple_attr"], (4, 5, 6))


    def test_to_dict_handles_dict_attributes(self):
        self.review.dict_attr = {"key": "value"}
        review_dict = self.review.to_dict()
        self.assertIn("dict_attr", review_dict)
        self.assertEqual(review_dict["dict_attr"], {"key": "value"})

    def test_to_dict_handles_float_attributes(self):
        self.review.float_attr = 10.11
        review_dict = self.review.to_dict()
        self.assertIn("float_attr", review_dict)
        self.assertEqual(review_dict["float_attr"], 10.11)

    def test_to_dict_handles_none_attributes(self):
        self.review.none_attr = None
        review_dict = self.review.to_dict()
        self.assertIn("none_attr", review_dict)
        self.assertEqual(review_dict["none_attr"], None)

    def test_to_dict_with_arg(self):
        """Tests to_dict method with an argument"""
        with self.assertRaises(TypeError):
            self.review.to_dict(12)

if __name__ == "__main__":
    unittest.main()
