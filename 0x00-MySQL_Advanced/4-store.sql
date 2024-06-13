-- 4-store.sql
-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS after_order_insert;

-- Create the trigger
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
