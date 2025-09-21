--Выберите уникальные регионы сбора грибов
select distinct name 
from regions;

--Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые»
select m.name, m.season, m.edible
from mushrooms m
join categories c on m.category_id = c.category_id
where c.name = 'Трубчатые';

--Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания
select c.name, count(m.mushroom_id) as mushroom_count
from categories c
left join mushrooms m on c.category_id = m.category_id
group by c.name
order by mushroom_count desc;

--Выведите название и описание съедобных грибов, которые лучше всего собирать в пяти самых больших по размеру (size) регионах
select m.name, m.description
from mushrooms m
join regions r on m.primary_region_id = r.region_id
where m.edible = TRUE
and r.region_id in (
	select region_id
	from regions
	order by size desc
	limit 5
);

-- Выведите названия всех грибов, которые растут весной, относятся к категории «Пластинчатые» и которые лучше всего собирать в местах размером до 6000 условных единиц (size)
select m.name
from mushrooms m
join categories c on m.category_id = c.category_id
join regions r on m.primary_region_id = r.region_id
where m.season = 'Весна'
and c.name = 'Пластинчатые'
and r.size <= 6000;

--Уникальные регионы: Используется DISTINCT для выборки уникальных названий регионов.

--Грибы категории «Трубчатые»: Используется JOIN для связи таблиц Mushrooms и Categories по category_id.

--Количество грибов по категориям: Группировка по категориям и подсчет количества грибов с использованием COUNT.

--Съедобные грибы в крупных регионах: Подзапрос выбирает 5 регионов с наибольшим размером, а основной запрос фильтрует съедобные грибы, собираемые в этих регионах.

--Грибы весной, категория «Пластинчатые», размер региона до 6000: Комбинируются условия для сезона, категории и размера региона.