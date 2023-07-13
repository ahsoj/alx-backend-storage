-- create a trigger that decreases the quantity of an items
-- afteradded a new order.
CREATE TRIGGER decrease_q AFTER INSERT ON orders
FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number
WHERE name=NEW.item_name;
